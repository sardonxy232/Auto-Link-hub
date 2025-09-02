from typing import Optional
from pydantic import BaseModel

# ---------------------
# User Schemas
# ---------------------
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# ---------------------
# Crop Schemas
# ---------------------
class CropBase(BaseModel):
    name: str
    description: Optional[str] = None

class CropCreate(CropBase):
    pass

class CropOut(CropBase):
    id: int

    class Config:
        from_attributes = True


# ---------------------
# Produce Schemas
# ---------------------
class ProduceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProduceCreate(ProduceBase):
    pass

class ProduceOut(ProduceBase):
    id: int
    farmer_id: int

    class Config:
        from_attributes = True


# ---------------------
# Supplier Schemas
# ---------------------
class SupplierItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class SupplierItemCreate(SupplierItemBase):
    pass

class SupplierItemOut(SupplierItemBase):
    id: int
    supplier_id: int

    class Config:
        from_attributes = True


# ---------------------
# Order Schemas
# ---------------------
class OrderBase(BaseModel):
    item_name: str
    quantity: int
    total_price: float

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int
    buyer_id: int
    status: str

    class Config:
        from_attributes = True


# ---------------------
# Logistics Schemas
# ---------------------
class LogisticsJobBase(BaseModel):
    description: str
    destination: str
    status: Optional[str] = "pending"

class LogisticsJobCreate(LogisticsJobBase):
    pass

class LogisticsJobOut(LogisticsJobBase):
    id: int
    logistics_id: int

    class Config:
        from_attributes = True
