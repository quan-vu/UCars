from sqlalchemy.orm import Session

from . import models, schemas


def get_car_brand(db: Session, id: int):
    return db.query(models.CarBrand).filter(models.CarBrand.id == id).first()


def get_car_brand_by_name(db: Session, name: str):
    return db.query(models.CarBrand).filter(models.CarBrand.name == name).first()


def get_car_brands(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CarBrand).offset(skip).limit(limit).all()


def create_car_brand(db: Session, car_brand: schemas.CarBrandCreate):
    try: 
        db_car_brand = models.CarBrand(**car_brand.dict())
        db.add(db_car_brand)
        db.commit()
        db.refresh(db_car_brand)
        return db_car_brand
    except:
        db.rollback()
        return None


def update_car_brand(db: Session, db_car_brand: schemas.CarBrand):
    db.add(db_car_brand)
    db.commit()
    db.refresh(db_car_brand)
    return db_car_brand


def delete_car_brand(db: Session, db_car_brand: schemas.CarBrand):
    try:
        db.delete(db_car_brand)
        db.commit()
        return True
    except:
        return False