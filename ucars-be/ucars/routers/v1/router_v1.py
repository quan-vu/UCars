from fastapi import APIRouter, Depends
from ucars.routers.v1 import root_route, car_brands_route, car_models_route


router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(root_route.router, tags=["Root"])
router_v1.include_router(car_brands_route.router, prefix="/car-brands", tags=["Car Brand"])
router_v1.include_router(car_models_route.router, prefix="/car-models", tags=["Car Model"])
