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


def user_create(user_data):
    if "name" not in user_data or "lastname" not in user_data:
        return None
    users = reading_users()
    max_user_id = max((user["id"] for user in users), default=0)
    new_user_id = max_user_id + 1
    new_user = {
        "id": new_user_id,
        "name": user_data["name"],
        "lastname": user_data["lastname"],
    }
    users.append(new_user)
    writing_users(users=users)
    return new_user
