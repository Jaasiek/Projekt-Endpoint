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


def get_all_users():
    return reading_users()
