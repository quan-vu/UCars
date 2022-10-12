from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, status
from ucars.repositories.car_brand_repository import CarBrandRepository
from ucars.dependencies import get_db
from ucars.schemas.car_brand_schema import CarBrandResponse, CarBrandCreate, CarBrandUpdate


router = APIRouter()


@router.get("/")
def read_car_brands(
    skip: int = 0, limit: int = 10, search_by: str = '', search_value: str = '',
    db: Session = Depends(get_db)
):
    car_brands = CarBrandRepository(db).paginate(skip=skip, limit=limit, search_by=search_by, search_value=search_value)
    return car_brands


@router.get("/{id}", response_model=CarBrandResponse)
def read_car_brand(id: int, db: Session = Depends(get_db)):
    car_brand = CarBrandRepository(db).find(id)
    if car_brand is None:
        raise HTTPException(status_code=404, detail="CarBrand not found")
    return car_brand


@router.post("/", response_model=CarBrandResponse, status_code=status.HTTP_201_CREATED)
def create_car_brand(car_brand: CarBrandCreate, db: Session = Depends(get_db)):
    db_car_brand = CarBrandRepository(db).find_by_name(car_brand.name)
    if db_car_brand:
        raise HTTPException(status_code=400, detail="Name already exists")
    car_brand = CarBrandRepository(db).create(car_brand)
    if car_brand is None:
        raise HTTPException(status_code=500, detail="Failed to create Car Brand")
    else:
        return car_brand


@router.put("/{id}", response_model=CarBrandResponse)
def update_car_brand(id: int, car_brand: CarBrandUpdate, db: Session = Depends(get_db)):
    db_car_brand = CarBrandRepository(db).find(id)
    if db_car_brand is None:
        raise HTTPException(status_code=404, detail="CarBrand not found")
    car_brand_data = car_brand.dict(exclude_unset=True)
    for key, value in car_brand_data.items():
        setattr(db_car_brand, key, value)
    return CarBrandRepository(db).update(db_car_brand)


@router.delete("/{id}")
def delete_car_brand(id: int, db: Session = Depends(get_db)):
    db_car_brand = CarBrandRepository(db).find(id)
    if db_car_brand is None:
        raise HTTPException(status_code=404, detail="CarBrand not found")
    CarBrandRepository(db).delete(db_car_brand)
    return {
        "message": "Car Brand was deleted successfully."
    }
