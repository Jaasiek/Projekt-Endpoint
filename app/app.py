from flask import Flask, request, jsonify
import controller


app = Flask(__name__)


@app.route("/")
def home_page():
    return "Server is running stable", 200


@app.route("/users")
def users_get():
    return jsonify(controller.users_get()), 200


@app.route("/users/<int:id>")
def single_user_get(id):
    user = controller.user_get(id)
    if user:
        return jsonify(user), 200
    return jsonify({"An error occurred": "User not found"}), 400


@app.route("/users", methods=["POST"])
def user_create():
    pass


@app.route("/users/<int:id>", methods=["PATCH"])
def user_update(id):
    pass


@app.route("/users/<int:id>", methods=["DELETE"])
def user_delete(id):
    pass


if __name__ == "__main__":
    app.run()
