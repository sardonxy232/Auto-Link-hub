# ----------------------------
# Produce CRUD
# ----------------------------
def create_produce(db: Session, produce: schemas.ProduceCreate, owner_id: int):
    db_produce = models.Produce(
        name=produce.name,
        description=produce.description,
        price=produce.price,
        quantity=produce.quantity,
        owner_id=owner_id
    )
    db.add(db_produce)
    db.commit()
    db.refresh(db_produce)
    return db_produce

def get_produce(db: Session, produce_id: int):
    return db.query(models.Produce).filter(models.Produce.id == produce_id).first()

def get_produces(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Produce).offset(skip).limit(limit).all()


# ----------------------------
# Supplier Items CRUD
# ----------------------------
def create_supplier_item(db: Session, item: schemas.SupplierItemCreate, supplier_id: int):
    db_item = models.SupplierItem(
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity,
        supplier_id=supplier_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_supplier_item(db: Session, item_id: int):
    return db.query(models.SupplierItem).filter(models.SupplierItem.id == item_id).first()

def get_supplier_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SupplierItem).offset(skip).limit(limit).all()


# ----------------------------
# Orders CRUD
# ----------------------------
def create_order(db: Session, order: schemas.OrderCreate, buyer_id: int):
    db_order = models.Order(
        item_name=order.item_name,
        quantity=order.quantity,
        total_price=order.total_price,
        buyer_id=buyer_id,
        status="pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()


# ----------------------------
# Logistics CRUD
# ----------------------------
def create_logistics_job(db: Session, job: schemas.LogisticsJobCreate, logistics_id: int):
    db_job = models.LogisticsJob(
        description=job.description,
        destination=job.destination,
        status=job.status,
        logistics_id=logistics_id
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_logistics_job(db: Session, job_id: int):
    return db.query(models.LogisticsJob).filter(models.LogisticsJob.id == job_id).first()

def get_logistics_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LogisticsJob).offset(skip).limit(limit).all()
