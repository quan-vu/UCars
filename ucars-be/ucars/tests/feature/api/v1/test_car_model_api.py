from pytest_schema import schema, Or
from faker import Faker

from fastapi.testclient import TestClient
from ucars.main import app

client = TestClient(app)
fake = Faker()


car_model_list_structure = {
  "total": int,
  "limit": int,
  "offset": int,
  "total_page": int,
  "next_page_link": Or(None, str),
  "data": [
    {
        "id": int,
        "name": str,
        "description": str,
        "car_brand_id": int,
        "is_active": bool,
        "created_at": Or(None, str),
        "updated_at": Or(None, str),
    }
  ]
}

car_model_detail_structure = {
    "id": int,
    "name": str,
    "description": Or(None, str),
    "car_brand_id": int,
    "is_active": bool,
}


class TestCardModelApi:

    def test_read_car_model_list(self):
        response = client.get("/v1/car-models/")
        data = response.json()
        assert response.status_code == 200
        assert schema(car_model_list_structure) == data

    def test_create_car_model_without_duplicate(self):
        payload = {
            "name": fake.uuid4(),
            "car_brand_id": fake.random_number(),
            "description": fake.text(),
            "is_active": True
        }
        response = client.post("/v1/car-models/", json=payload)
        data = response.json()

        assert response.status_code == 201
        assert data['is_active'] == payload['is_active']
        assert data['name'] == payload['name']
        assert schema(car_model_detail_structure) == response.json()

    def test_create_car_model_with_duplicated(self):
        payload = {
            "name": fake.uuid4(),
            "car_brand_id": fake.random_number(),
            "description": fake.text(),
            "is_active": True
        }

        # Create car model the first times
        response = client.post("/v1/car-models/", json=payload)

        # Create car model the second times
        response = client.post("/v1/car-models/", json=payload)

        assert response.status_code == 400
        assert response.json() == {"detail": "Name already exists"}

    def test_update_car_model(self):
        payload = {
            "name": fake.uuid4(),
            "car_brand_id": fake.random_number(),
            "description": fake.text(),
            "is_active": True
        }

        # Create car model the first times
        response = client.post("/v1/car-models/", json=payload)
        created_obj = response.json()

        # Update car model
        payload['description'] = 'my description'
        response = client.put(f"/v1/car-models/{created_obj['id']}", json=payload)
        updated_obj = response.json()

        assert response.status_code == 200
        assert updated_obj['description'] == 'my description'

    def test_delete_car_model(self):
        # Create car model the first times
        payload = {
            "name": fake.uuid4(),
            "car_brand_id": fake.random_number(),
            "description": fake.text(),
            "is_active": True
        }
        response = client.post("/v1/car-models/", json=payload)
        created_obj = response.json()

        # Delete car model
        response = client.delete(f"/v1/car-models/{created_obj['id']}")
        assert response.status_code == 200

        # Get car model
        response = client.get(f"/v1/car-models/{created_obj['id']}")
        assert response.status_code == 404
