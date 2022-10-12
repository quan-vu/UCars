from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base_model import BaseModel


class CarBrand(BaseModel):
    __tablename__ = "car_brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    logo = Column(String, default=None)
    description = Column(String, default=None)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)

    car_models = relationship("CarModel", back_populates="car_brand")


class CarModel(BaseModel):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    car_brand_id = Column(Integer, ForeignKey("car_brands.id"))
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)

    car_brand = relationship("CarBrand", back_populates="car_models")
