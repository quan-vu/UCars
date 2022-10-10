from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="UCars API",
    description="Cars Management System",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Github",
        "url": "https://github.com/quan-vu/UCars",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)


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


# Car Brand API
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


# Car Model API
@app.post("/car_models/", response_model=schemas.CarModel)
def create_car_model(car_model: schemas.CarModelCreate, db: Session = Depends(get_db)):
    db_car_model = crud.get_car_model_by_name(db, name=car_model.name)
    if db_car_model:
        raise HTTPException(status_code=400, detail="Name already registered")
    car_model = crud.create_car_model(db=db, car_model=car_model, )
    if car_model is None:
        raise HTTPException(status_code=500, detail="Failed to create Car Model")
    else:
        return car_model


@app.get("/car_models/", response_model=List[schemas.CarModel])
def read_car_models(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    car_models = crud.get_car_models(db, skip=skip, limit=limit)
    return car_models


@app.get("/car_models/{id}", response_model=schemas.CarModel)
def read_car_model(id: int, db: Session = Depends(get_db)):
    db_car_model = crud.get_car_model(db, id=id)
    if db_car_model is None:
        raise HTTPException(status_code=404, detail="CarModel not found")
    return db_car_model


@app.put("/car_models/{id}", response_model=schemas.CarModel)
def update_car_model(id: int, car_model: schemas.CarModelUpdate, db: Session = Depends(get_db)):
    db_car_model = crud.get_car_model(db, id=id)
    if db_car_model is None:
        raise HTTPException(status_code=404, detail="CarModel not found")
    car_model_data = car_model.dict(exclude_unset=True)
    for key, value in car_model_data.items():
        setattr(db_car_model, key, value)
    return crud.update_car_model(db, db_car_model)


@app.delete("/car_models/{id}")
def delete_car_model(id: int, db: Session = Depends(get_db)):
    db_car_model = crud.get_car_model(db, id=id)
    if db_car_model is None:
        raise HTTPException(status_code=404, detail="CarModel not found")
    success = crud.delete_car_model(db, db_car_model)
    if success:
        return {
            "message": "Car Model was deleted successfully."
        }
    else:
        raise HTTPException(status_code=404, detail="Failed to delete Car Model")