from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello world"}


def test_read_category():
    response = client.get('/api/v1/category?name=축산')
    assert response.status_code == 200
    print("데이터:",response.json())
    assert response.json()['category_name'] == "축산"
