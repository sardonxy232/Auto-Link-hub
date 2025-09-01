# app/main.py
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import create_access_token, get_current_user, role_required
from datetime import timedelta
from app.schemas import CropCreate, CropOut
from app.crud import create_crop, get_crops, update_crop, delete_crop
# app/main.py
from fastapi import FastAPI, Depends
from app import models, schemas, crud, auth, database
from sqlalchemy.orm import Session


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # create JWT
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/farmers")
def get_farmers(user=Depends(role_required("farmer"))):
    return {"message": f"Hello Farmer {user.email}, here are your crops!"}

@app.get("/buyers")
def get_buyers(user=Depends(role_required("buyer"))):
    return {"message": f"Hello Buyer {user.email}, here are the available products!"}

@app.get("/suppliers")
def get_suppliers(user=Depends(role_required("supplier"))):
    return {"message": f"Hello Supplier {user.email}, here are the requests for tools/fertilizers!"}

@app.get("/logistics")
def get_logistics(user=Depends(role_required("logistics"))):
    return {"message": f"Hello Logistics {user.email}, here are the delivery requests!"}

@app.get("/me", response_model=schemas.UserOut)
def read_users_me(current_user=Depends(get_current_user)):
    return current_user


@app.post("/crops/", response_model=CropOut)
def create_crop_for_farmer(
    crop: CropCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can add crops")
    return create_crop(db=db, crop=crop, farmer_id=current_user.id)


@app.get("/crops/", response_model=list[CropOut])
def list_crops(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_crops(db=db, skip=skip, limit=limit)

@app.put("/crops/{crop_id}", response_model=CropOut)
def update_crop_for_farmer(
    crop_id: int,
    crop: CropCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can update crops")
    
    updated = update_crop(db=db, crop_id=crop_id, crop=crop, farmer_id=current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Crop not found or unauthorized")
    return updated


@app.delete("/crops/{crop_id}", response_model=CropOut)
def delete_crop_for_farmer(
    crop_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can delete crops")
    
    deleted = delete_crop(db=db, crop_id=crop_id, farmer_id=current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Crop not found or unauthorized")
    return deleted


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return auth.login_user(db=db, user=user)

# ✅ New endpoint: Get current user
@app.get("/users/me", response_model=schemas.UserOut)
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user

