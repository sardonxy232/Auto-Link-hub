# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext
from app.auth import verify_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_crop(db: Session, crop: schemas.CropCreate, farmer_id: int):
    db_crop = models.Crop(
        name=crop.name,
        description=crop.description,
        price=crop.price,
        quantity=crop.quantity,
        farmer_id=farmer_id
    )
    db.add(db_crop)
    db.commit()
    db.refresh(db_crop)
    return db_crop

def get_crops(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Crop).offset(skip).limit(limit).all()
