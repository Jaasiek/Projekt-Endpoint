import pytest
from flask import Flask
from app.app import app
from app.controller import *


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_flask_app_exists() -> None:
    assert isinstance(app, Flask)


def test_users_get() -> None:
    pass


def test_user_get() -> None:
    with app.test_request_context():
        assert user_get(1)[1] == 200


def test_post_user() -> None:
    response = client.post("/users", json={"name": "Leszek", "lastname": "Gawęda"})
    assert response.status_code == 201


def test_patch_user() -> None:
    response = client.patch("/users/3", json={"name": "Kuba", "lastname": "Sawulski"})
    assert response.status_code == 204


def test_patch_user_error_1() -> None:
    response = client.patch(
        "/users/2137", json={"name": "Kuba", "lastname": "Sawulski"}
    )
    assert response.status_code == 400


def test_patch_user_error_2() -> None:
    response = client.patch("/users/2", json={"imię": "Kuba", "nazwisko": "Sawulski"})
    assert response.status_code == 400


def test_put_user() -> None:
    response = client.put("/users/4", json={"name": "Dawid", "lastname": "Markiewicz"})
    assert response.status_code == 204


def test_delete_user() -> None:
    response = client.delete("/users/2")
    assert response.status_code == 204


def test_delete_user_error() -> None:
    response = client.delete("/users/2137")
    assert response.status_code == 400
