# app/schemas.py
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional


# Role Enum
class UserRole(str, Enum):
    farmer = "farmer"
    buyer = "buyer"
    supplier = "supplier"
    logistics = "logistics"

# Base user shared props
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole

# Schema for creating a new user (signup)
class UserCreate(UserBase):
    password: str

# Schema for showing user data (no password exposure)
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # For SQLAlchemy -> Pydantic



class CropBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class CropCreate(CropBase):
    pass

class CropOut(CropBase):
    id: int
    farmer_id: int

    class Config:
        orm_mode = True
