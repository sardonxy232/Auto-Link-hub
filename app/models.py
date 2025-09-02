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
    supplier_items = relationship("SupplierItem", back_populates="supplier")
    orders = relationship("Order", back_populates="buyer")
    logistics_jobs = relationship("LogisticsJob", back_populates="logistics")


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


# ---------------------
# Supplier Item Model
# ---------------------
class SupplierItem(Base):
    __tablename__ = "supplier_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    supplier = relationship("User", back_populates="supplier_items")


# ---------------------
# Order Model
# ---------------------
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="pending")
    buyer_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    buyer = relationship("User", back_populates="orders")


# ---------------------
# Logistics Job Model
# ---------------------
class LogisticsJob(Base):
    __tablename__ = "logistics_jobs"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    status = Column(String, default="pending")
    logistics_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    logistics = relationship("User", back_populates="logistics_jobs")
    