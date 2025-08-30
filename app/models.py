# app/models.py
from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from app.database import Base
import enum
from sqlalchemy.orm import relationship
from app.database import Base

# Define possible roles
class UserRole(enum.Enum):
    farmer = "farmer"
    buyer = "buyer"
    supplier = "supplier"
    logistics = "logistics"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

class Crop(Base):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    farmer_id = Column(Integer, ForeignKey("users.id"))

    farmer = relationship("User")

