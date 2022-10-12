from typing import Union
from pydantic import BaseModel


class CarModelBase(BaseModel):
    name: str
    description: Union[str, None] = None
    is_active: bool


class CarModelCreate(CarModelBase):
    car_brand_id: int


class CarModelUpdate(CarModelBase):
    name: Union[str, None] = None
    description: Union[str, None] = None
    car_brand_id: Union[int, None] = None
    is_active: Union[bool, None] = None


class CarModelResponse(CarModelBase):
    id: int
    car_brand_id: int

    class Config:
        orm_mode = True
