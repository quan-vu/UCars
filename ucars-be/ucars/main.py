from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to UCars!"}


@app.post("/car_brands/", response_model=schemas.CarBrand)
def create_car_brand(car_brand: schemas.CarBrandCreate, db: Session = Depends(get_db)):
    db_car_brand = crud.get_car_brand_by_name(db, name=car_brand.name)
    if db_car_brand:
        raise HTTPException(status_code=400, detail="Name already registered")
    car_brand = crud.create_car_brand(db=db, car_brand=car_brand)
    if car_brand is None:
        raise HTTPException(status_code=500, detail="Failed to create Car Brand")
    else:
        return car_brand


@app.get("/car_brands/", response_model=List[schemas.CarBrand])
def read_car_brands(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    car_brands = crud.get_car_brands(db, skip=skip, limit=limit)
    return car_brands


@app.get("/car_brands/{id}", response_model=schemas.CarBrand)
def read_car_brand(id: int, db: Session = Depends(get_db)):
    db_car_brand = crud.get_car_brand(db, id=id)
    if db_car_brand is None:
        raise HTTPException(status_code=404, detail="CarBrand not found")
    return db_car_brand


@app.put("/car_brands/{id}", response_model=schemas.CarBrand)
def update_car_brand(id: int, car_brand: schemas.CarBrandUpdate, db: Session = Depends(get_db)):
    db_car_brand = crud.get_car_brand(db, id=id)
    if db_car_brand is None:
        raise HTTPException(status_code=404, detail="CarBrand not found")
    car_brand_data = car_brand.dict(exclude_unset=True)
    for key, value in car_brand_data.items():
        setattr(db_car_brand, key, value)
    return crud.update_car_brand(db, db_car_brand)


@app.delete("/car_brands/{id}")
def delete_car_brand(id: int, db: Session = Depends(get_db)):
    db_car_brand = crud.get_car_brand(db, id=id)
    if db_car_brand is None:
        raise HTTPException(status_code=404, detail="CarBrand not found")
    success = crud.delete_car_brand(db, db_car_brand)
    if success:
        return {
            "message": "Car Brand was deleted successfully."
        }
    else:
        raise HTTPException(status_code=404, detail="Failed to delete Car Brand")
