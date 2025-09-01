# app/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

# ---------------------
# Role Enum
# ---------------------
class UserRole(enum.Enum):
    farmer = "farmer"
    buyer = "buyer"
    supplier = "supplier"
    logistics = "logistics"

# ---------------------
# User Model
# ---------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.farmer, nullable=False)

    # Relationships
    produces = relationship("Produce", back_populates="owner")
    crops = relationship("Crop", back_populates="farmer")

# ---------------------
# Crop Model
# ---------------------
class Crop(Base):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    image = Column(String, nullable=True)  # Optional crop image
    farmer_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    farmer = relationship("User", back_populates="crops")

# ---------------------
# Produce Model
# ---------------------
class Produce(Base):
    __tablename__ = "produces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    image = Column(String, nullable=True)  # URL or path to the image
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    owner = relationship("User", back_populates="produces")
