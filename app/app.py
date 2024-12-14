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


if __name__ == "__main__":
    app.run()
