# app/main.py
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schemas, crud, auth, database
from app.auth import create_access_token, get_current_user, role_required

# ---------------------
# Database setup
# ---------------------
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------
# Authentication
# ---------------------

@app.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.UserOut)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

# ---------------------
# Role-Based Endpoints
# ---------------------

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

# ---------------------
# Crop Endpoints
# ---------------------

@app.post("/crops/", response_model=schemas.CropOut)
def create_crop_for_farmer(
    crop: schemas.CropCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can add crops")
    return crud.create_crop(db=db, crop=crop, farmer_id=current_user.id)

@app.get("/crops/", response_model=list[schemas.CropOut])
def list_crops(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_crops(db=db, skip=skip, limit=limit)

@app.put("/crops/{crop_id}", response_model=schemas.CropOut)
def update_crop_for_farmer(
    crop_id: int,
    crop: schemas.CropCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can update crops")
    
    updated = crud.update_crop(db=db, crop_id=crop_id, crop=crop, farmer_id=current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Crop not found or unauthorized")
    return updated

@app.delete("/crops/{crop_id}", response_model=schemas.CropOut)
def delete_crop_for_farmer(
    crop_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can delete crops")
    
    deleted = crud.delete_crop(db=db, crop_id=crop_id, farmer_id=current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Crop not found or unauthorized")
    return deleted

# ---------------------
# Produce Endpoints
# ---------------------

@app.post("/produces/", response_model=schemas.ProduceOut)
def create_produce(
    produce: schemas.ProduceCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can create produce")
    return crud.create_produce(db=db, produce=produce, user_id=current_user.id)

@app.get("/produces/", response_model=list[schemas.ProduceOut])
def read_produces(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_produces(db=db, skip=skip, limit=limit)

@app.get("/produces/{produce_id}", response_model=schemas.ProduceOut)
def read_produce(produce_id: int, db: Session = Depends(get_db)):
    db_produce = crud.get_produce_by_id(db, produce_id)
    if not db_produce:
        raise HTTPException(status_code=404, detail="Produce not found")
    return db_produce

@app.put("/produces/{produce_id}", response_model=schemas.ProduceOut)
def update_produce(
    produce_id: int,
    produce: schemas.ProduceUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_produce = crud.get_produce_by_id(db, produce_id)
    if not db_produce:
        raise HTTPException(status_code=404, detail="Produce not found")
    if db_produce.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this produce")
    return crud.update_produce(db, produce_id, produce)

@app.delete("/produces/{produce_id}")
def delete_produce(
    produce_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_produce = crud.get_produce_by_id(db, produce_id)
    if not db_produce:
        raise HTTPException(status_code=404, detail="Produce not found")
    if db_produce.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this produce")
    crud.delete_produce(db, produce_id)
    return {"status": "deleted"}
