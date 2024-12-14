import pytest
import json
import os
from ...app.controller import (
    user_create,
    user_delete,
    user_get,
    users_get,
    user_replace,
    user_update,
    reading_users,
    writing_users,
)


@pytest.fixture
def test_get_users():
    read_users = reading_users()
    users = users_get()
    assert len(users) == len(users_get)


def test_get_single_user():
    users = reading_users()
    if users:
        user_id = users[0]["id"]
        user = user_get(user_id)
        assert user is not None
        assert user["id"] == user_id
    else:
        pytest.skip("Empty file")


def adding_user():
    new_user = {"name": "Filip", "lastname": "Łoniakowski"}
    user_adding = adding_user(new_user)
    assert user_adding["name"] == "Filip"
    assert user_adding["lastname"] == "Łoniakowski"
    users = reading_users()
    assert any(user["id"] == user_adding["id"] for user in users)


def modify_user():
    pass
