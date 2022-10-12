from typing import List, Optional, Union

from pydantic import BaseModel


# Car Model
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


class CarModel(CarModelBase):
    id: int
    car_brand_id: int

    class Config:
        orm_mode = True


# Car Brand
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


class CarBrand(CarBrandBase):
    id: int
    is_active: bool
    models: List[CarModel] = []

    class Config:
        orm_mode = True
