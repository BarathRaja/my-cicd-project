from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_create_item_success():
    response = client.post("/items/", json={"name": "Keyboard", "price": 45.99})
    assert response.status_code == 200

def test_create_item_negative_price():
    response = client.post("/items/", json={"name": "Debt", "price": -10.00})
    assert response.status_code == 400

def test_create_item_missing_field():
    response = client.post("/items/", json={"name": "Freebie"})
    assert response.status_code == 422

def test_secure_data_authorized(monkeypatch):
    monkeypatch.setenv("TEST_DB_PASSWORD", "super_secret_123")
    response = client.get("/secure-data/")
    assert response.status_code == 200

def test_secure_data_unauthorized(monkeypatch):
    monkeypatch.setenv("TEST_DB_PASSWORD", "wrong_password")
    response = client.get("/secure-data/")
    assert response.status_code == 401
