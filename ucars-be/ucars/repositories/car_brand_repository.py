from ucars.repositories.base_repository import BaseRepository
from ucars.models.car_brand import CarBrand


class CarBrandRepository(BaseRepository):

    model = CarBrand

    def find_by_name(self, name: str):
        return self.db.query(self.model).filter(self.model.name == name).first()
