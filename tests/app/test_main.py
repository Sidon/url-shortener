from fastapi.testclient import TestClient
from src.app.main import app
from src.cross import data_helper


client = TestClient(app)

def test_read_root_whithout_url():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == data_helper.WELLCOME_MESSAGE


def test_read_root_whith_invalid_url():
    response = client.get("/", params={"shortened_url": data_helper.BAD_PARAMETER_URL})
    assert response.status_code == 422
    assert response.json()['detail'] == data_helper.BAD_URL_MESSAGE

def test_read_root_whith_invalid_url():
    response = client.get("/", params={"shortened_url": data_helper.BAD_PARAMETER_URL})
    assert response.status_code == 400
    assert response.json()['detail'] == data_helper.BAD_URL_MESSAGE

def test_create_whith_invalid_url():
    response = client.post("/create", params={"target_url": data_helper.BAD_PARAMETER_URL})
    assert response.status_code == 400
    assert response.json()['detail'] == data_helper.BAD_URL_MESSAGE