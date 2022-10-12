from ucars.repositories.base_repository import BaseRepository
from ucars.models.car_brand import CarModel


class CarModelRepository(BaseRepository):

    model = CarModel

    def find_by_name(self, name: str):
        return self.db.query(self.model).filter(self.model.name == name).first()
