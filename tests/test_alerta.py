import pytest
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient

from routers.alerta import router

client = TestClient(router)


def test_should_return_method_not_allowed_when_requests_is_not_post():
    response = client.get("/alerta/")
    assert response.status_code == 405


def test_should_return_alert_when_params_are_valid():
    response = client.post(
        "/alerta/",
        json={
            "event": "event",
            "resource": "resource",
            "severity": "severity",
            "notes": "notes",
        },
    )
    assert response.status_code == 200


def test_should_return_same_values_passed_in_params():
    response = client.post(
        "/alerta/",
        json={
            "event": "event",
            "resource": "resource",
            "severity": "severity",
            "notes": "notes",
        },
    )
    assert response.json() == {
        "event": "event",
        "resource": "resource",
        "severity": "severity",
        "notes": "notes",
    }


def test_should_return_422_when_notes_is_not_string():
    with pytest.raises(RequestValidationError):
        response = client.post(
            "/alerta/",
            json={
                "event": "event",
                "resource": "resource",
                "severity": "severity",
                "notes": 1,
            },
        )
