from typing import List, Optional, Union
from pydantic import BaseModel
from ucars.schemas.car_model_schema import CarModelResponse


class CarBrandBase(BaseModel):
    name: str
    logo: Union[str, None] = None
    description: Union[str, None] = None
    is_active: bool


class CarBrandCreate(CarBrandBase):
    # use all column from base
    pass


class CarBrandUpdate(CarBrandBase):
    name: Optional[str] = None
    logo: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class CarBrandResponse(CarBrandBase):
    id: int
    is_active: bool
    models: List[CarModelResponse] = []

    class Config:
        orm_mode = True
