from typing import List, Optional, Union

from pydantic import BaseModel


class CarModelBase(BaseModel):
    name: str
    description: Union[str, None] = None


class CarModelCreate(CarModelBase):
    pass


class CarModel(CarModelBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CarBrandBase(BaseModel):
    name: str
    logo: str
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
