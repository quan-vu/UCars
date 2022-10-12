from fastapi.testclient import TestClient
from ucars.main import app

client = TestClient(app)


def test_read_car_brand_list():
    response = client.get("/v2/car-brands")
    assert response.status_code == 404
