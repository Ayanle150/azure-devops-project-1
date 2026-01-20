from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_ok():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert "version" in data
    assert "git_sha" in data

def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["health"] == "healthy"
