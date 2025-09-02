# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, get_db
from fastapi.staticfiles import StaticFiles
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Agric Link Hub API 🚜🌱",
    description="API for managing users, authentication, and products",
    version="1.0.0",
    docs_url="/docs",   # Swagger UI
    redoc_url="/redoc", # ReDoc
    openapi_url="/openapi.json"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Agric Link Hub API 🚜🌱",
        "docs": "/docs",
        "redoc": "/redoc"
    }


# ---------------------
# Suppliers Endpoints
# ---------------------
@app.post("/suppliers/", response_model=schemas.SupplierItemOut)
def create_supplier_item(item: schemas.SupplierItemCreate, db: Session = Depends(get_db)):
    db_item = models.SupplierItem(**item.dict(), supplier_id=1)  # Replace with actual logged-in supplier
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/suppliers/", response_model=list[schemas.SupplierItemOut])
def read_supplier_items(db: Session = Depends(get_db)):
    return db.query(models.SupplierItem).all()

@app.get("/suppliers/{item_id}", response_model=schemas.SupplierItemOut)
def read_supplier_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.SupplierItem).filter(models.SupplierItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Supplier item not found")
    return db_item

@app.delete("/suppliers/{item_id}")
def delete_supplier_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.SupplierItem).filter(models.SupplierItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Supplier item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Supplier item deleted successfully"}


# ---------------------
# Orders Endpoints
# ---------------------
@app.post("/orders/", response_model=schemas.OrderOut)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(**order.dict(), buyer_id=1, status="pending")  # Replace with actual buyer
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.get("/orders/", response_model=list[schemas.OrderOut])
def read_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@app.get("/orders/{order_id}", response_model=schemas.OrderOut)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"detail": "Order deleted successfully"}


# ---------------------
# Logistics Endpoints
# ---------------------
@app.post("/logistics/", response_model=schemas.LogisticsJobOut)
def create_logistics_job(job: schemas.LogisticsJobCreate, db: Session = Depends(get_db)):
    db_job = models.LogisticsJob(**job.dict(), logistics_id=1)  # Replace with actual logistics user
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@app.get("/logistics/", response_model=list[schemas.LogisticsJobOut])
def read_logistics_jobs(db: Session = Depends(get_db)):
    return db.query(models.LogisticsJob).all()

@app.get("/logistics/{job_id}", response_model=schemas.LogisticsJobOut)
def read_logistics_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(models.LogisticsJob).filter(models.LogisticsJob.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Logistics job not found")
    return db_job

@app.delete("/logistics/{job_id}")
def delete_logistics_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(models.LogisticsJob).filter(models.LogisticsJob.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Logistics job not found")
    db.delete(db_job)
    db.commit()
    return {"detail": "Logistics job deleted successfully"}
