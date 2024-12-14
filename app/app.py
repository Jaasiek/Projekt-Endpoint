from flask import Flask, jsonify
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
    return jsonify({"error": "User not found"}), 400


if __name__ == "__main__":
    app.run()
