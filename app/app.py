from flask import Flask, request, jsonify
import json


app = Flask(__name__)


def reading_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def writing_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=1)


@app.route("/")
def home_page():
    return "Server is running stable", 200


@app.route("/users")
def users_get():
    users = reading_users()
    return jsonify(reading_users), 200


@app.route("/users/<int:id>")
def single_user_get(id):
    users = reading_users()

    for user in users:
        if user["id"] == id:
            wanted = user
            break
    if wanted:
        return jsonify(wanted), 200
    return jsonify({"error occurred": "User not found"}), 400


@app.route("/users", methods=["POST"])
def user_create():
    path_data = request.get_json()
    if "name" in user and "lastname" in user:
        users = reading_users()
        max_users_id = 0
        for user in users:
            if user["id"] > max_users_id:
                max_users_id = user["id"]
        new_user_id = max_users_id + 1
        new_user = {
            "id": new_user_id,
            "name": path_data["name"],
            "lastname": path_data["lastname"],
        }
        users.append(new_user)
        writing_users(users=users)
        return jsonify(new_user), 200
    return jsonify({"error occurred": "Invalid request"}), 400


@app.route("/users/<int:id>", methods=["PATCH"])
def user_update(id):
    path_data = request.get_json()
    users = reading_users()
    for user in users:
        if user["id"] == id:
            wanted = user
            break
    if wanted:
        if "name" in path_data:
            wanted["name"] = path_data["name"]
        if "lastname" in path_data:
            wanted["lastname"] = path_data["lastname"]
        writing_users(users=users)
        return "User updated succesfully", 204

    return jsonify({"error occurred": "Invalid request"}), 400


if __name__ == "__main__":
    app.run()
