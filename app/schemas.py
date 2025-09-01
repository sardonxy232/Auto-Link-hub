# app/schemas.py
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

# ---------------------
# Role Enum
# ---------------------
class UserRole(str, Enum):
    farmer = "farmer"
    buyer = "buyer"
    supplier = "supplier"
    logistics = "logistics"

# ---------------------
# User Schemas
# ---------------------
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode

# ---------------------
# Crop Schemas
# ---------------------
class CropBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class CropCreate(CropBase):
    pass

class CropOut(CropBase):
    id: int
    image: Optional[str]
    farmer_id: int

    class Config:
        from_attributes = True

# ---------------------
# Produce Schemas
# ---------------------
class ProduceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ProduceCreate(ProduceBase):
    pass

class ProduceUpdate(ProduceBase):
    pass

class ProduceOut(ProduceBase):
    id: int
    image: Optional[str]
    owner_id: int

    class Config:
        from_attributes = True

# ---------------------
# Auth Schemas
# ---------------------
class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
