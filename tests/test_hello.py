from fastapi.testclient import TestClient

from routers.hello import router

client = TestClient(router)


def test_should_return_hello_name_when_name_provided():
    response = client.get("/hello/richard")
    assert response.json() == {"message": "Hello richard"}


def test_should_return_200_when_path_is_provided():
    response = client.get("/hello/richard")
    assert response.status_code == 200


def test_should_return_404_when_path_is_empty():
    response = client.get("/hello/")
    assert response.status_code == 404
