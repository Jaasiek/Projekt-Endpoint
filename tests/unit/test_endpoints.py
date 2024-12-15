import pytest

from ...app.controller import *


@pytest.fixture
def test_get_users():
    read_users = reading_users()
    users = users_get()
    assert len(users) == len(read_users)


def test_get_single_user():
    users = reading_users()

    user_id = users[0]["id"]
    user = user_get(user_id)
    assert user is not None
    assert user["id"] == user_id


def test_adding_user():
    new_user = {"name": "Filip", "lastname": "Łoniakowski"}
    user_adding = user_create(new_user)
    assert user_adding["name"] == "Filip"
    assert user_adding["lastname"] == "Łoniakowski"
    users = reading_users()
    assert any(user["id"] == user_adding["id"] for user in users)


def test_modify_user():
    users = reading_users()

    user_id = users[0]["id"]
    updating = user_update(user_id, {"name": "Tomasz"})
    assert updating

    users = reading_users()
    updated_user = next(user for user in users if user["id"] == user_id)
    assert updated_user["name"] == "Tomasz"


def test_replacing_user():
    users = reading_users()

    user_id = users[0]["id"]
    user_replacing = user_replace(user_id, {"name": "Adam", "lastname": "Kużma"})
    assert user_replacing

    users = reading_users()
    user_replacing = next(user for user in users if user["id"] == user_id)
    assert user_replacing["name"] == "Adam"


def test_deleting_user():
    users = reading_users()

    user_id = users[0]["id"]
    user_to_delete = user_delete(user_id)
    assert user_to_delete

    users = reading_users()
    assert not any(user["id"] == user_id for user in users)
