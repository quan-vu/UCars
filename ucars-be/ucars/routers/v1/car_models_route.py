from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, status
from ucars.repositories.car_model_repository import CarModelRepository
from ucars.dependencies import get_db
from ucars.schemas.car_model_schema import CarModelCreate, CarModelUpdate, CarModelResponse


router = APIRouter()


@router.get("/")
def read_car_models(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)): 
    car_models = CarModelRepository(db).get()
    car_models = CarModelRepository(db).paginate(skip=skip, limit=limit)
    return car_models


@router.get("/{id}", response_model=CarModelResponse)
def read_car_model(id: int, db: Session = Depends(get_db)):
    car_model = CarModelRepository(db).find(id)
    if car_model is None:
        raise HTTPException(status_code=404, detail="CarModel not found")
    return car_model


@router.post("/", response_model=CarModelResponse, status_code=status.HTTP_201_CREATED)
def create_car_model(car_model: CarModelCreate, db: Session = Depends(get_db)):
    db_car_model = CarModelRepository(db).find_by_name(car_model.name)
    if db_car_model:
        raise HTTPException(status_code=400, detail="Name already exists")
    car_model = CarModelRepository(db).create(car_model)
    if car_model is None:
        raise HTTPException(status_code=500, detail="Failed to create Car Model")
    else:
        return car_model



@router.put("/{id}", response_model=CarModelResponse)
def update_car_model(id: int, car_model: CarModelUpdate, db: Session = Depends(get_db)):
    db_car_model = CarModelRepository(db).find(id)
    if db_car_model is None:
        raise HTTPException(status_code=404, detail="CarModel not found")
    car_model_data = car_model.dict(exclude_unset=True)
    for key, value in car_model_data.items():
        setattr(db_car_model, key, value)
    return CarModelRepository(db).update(db_car_model)


@router.delete("/{id}")
def delete_car_model(id: int, db: Session = Depends(get_db)):
    db_car_model = CarModelRepository(db).find(id)
    if db_car_model is None:
        raise HTTPException(status_code=404, detail="CarModel not found")
    CarModelRepository(db).delete(db_car_model)
    return {
        "message": "Car Model was deleted successfully."
    }