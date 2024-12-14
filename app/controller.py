import json


def reading_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def writing_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)


def users_get():
    return reading_users()


def user_get(id):
    users = reading_users()
    for user in users:
        if user["id"] == id:
            return user
    return None
