from pytest_schema import schema, Or
from faker import Faker

from fastapi.testclient import TestClient
from ucars.main import app

client = TestClient(app)
fake = Faker()


car_brand_list_structure = {
  "total": int,
  "limit": int,
  "offset": int,
  "total_page": int,
  "next_page_link": Or(None, str),
  "data": [
    {
      "id": int,
      "logo": Or(None, str),
      "name": str,
      "description": Or(None, str),
      "is_active": bool,
      "created_at": Or(None, str),
      "updated_at": Or(None, str),
    }
  ]
}

car_brand_detail_structure = {
    "id": int,
    "logo": Or(None, str),
    "name": str,
    "description": Or(None, str),
    "is_active": bool,
    "models": []
}


class TestCardBrandApi:

    def test_read_car_brand_list(self):
        response = client.get("/v1/car-brands/")
        data = response.json()
        assert response.status_code == 200
        assert schema(car_brand_list_structure) == data

    def test_create_car_brand_without_duplicate(self):
        payload = {
            "name": fake.uuid4(),
            "logo": fake.text(),
            "description": fake.text(),
            "is_active": True
        }
        response = client.post("/v1/car-brands/", json=payload)
        data = response.json()

        assert response.status_code == 201
        assert data['is_active'] == payload['is_active']
        assert data['name'] == payload['name']
        assert schema(car_brand_detail_structure) == response.json()

    def test_create_car_brand_with_duplicated(self):
        payload = {
            "name": fake.uuid4(),
            "logo": fake.text(),
            "description": fake.text(),
            "is_active": True
        }

        # Create car brand the first times
        response = client.post("/v1/car-brands/", json=payload)

        # Create car brand the second times
        response = client.post("/v1/car-brands/", json=payload)

        assert response.status_code == 400
        assert response.json() == {"detail": "Name already exists"}

    def test_update_car_brand(self):
        payload = {
            "name": fake.uuid4(),
            "logo": fake.text(),
            "description": fake.text(),
            "is_active": True
        }

        # Create car brand the first times
        response = client.post("/v1/car-brands/", json=payload)
        created_obj = response.json()

        # Update car brand
        payload['logo'] = 'my logo'
        response = client.put(f"/v1/car-brands/{created_obj['id']}", json=payload)
        updated_obj = response.json()

        assert response.status_code == 200
        assert updated_obj['logo'] == 'my logo'

    def test_delete_car_brand(self):
        # Create car brand the first times
        payload = {
            "name": fake.uuid4(),
            "logo": fake.text(),
            "description": fake.text(),
            "is_active": True
        }
        response = client.post("/v1/car-brands/", json=payload)
        created_obj = response.json()

        # Delete car brand
        response = client.delete(f"/v1/car-brands/{created_obj['id']}")
        assert response.status_code == 200

        # Get car brand
        response = client.get(f"/v1/car-brands/{created_obj['id']}")
        assert response.status_code == 404
