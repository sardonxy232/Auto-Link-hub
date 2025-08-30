# app/models.py
from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

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
