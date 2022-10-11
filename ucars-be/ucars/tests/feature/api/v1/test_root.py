from fastapi.testclient import TestClient
from ucars.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to UCars API V1!"}
