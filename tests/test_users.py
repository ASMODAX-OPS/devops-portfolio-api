from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_user():
    response = client.post("/api/users", json={"name": "Ana", "email": "ana@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Ana"
    assert "id" in data

    user_id = data["id"]
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "ana@example.com"

def test_list_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_nonexistent_user():
    response = client.get("/api/users/99999")
    assert response.status_code == 404