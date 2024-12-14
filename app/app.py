from flask import Flask, request, jsonify
import controller


app = Flask(__name__)


@app.get("/")
def home_page():
    return "Server is running stable", 200


@app.get("/users")
def users_get():
    return jsonify(controller.users_get()), 200


@app.get("/users/<int:id>")
def single_user_get(id):
    user = controller.user_get(id)
    if user:
        return jsonify(user), 200
    return jsonify({"An error occurred": "User not found"}), 400


@app.post("/users")
def user_create():
    user_data = request.get_json()
    new_user = controller.user_create(user_data)
    if new_user:
        return jsonify(new_user), 201


@app.patch("/users/<int:id>")
def user_update(id):
    user_data = request.get_json()
    if controller.user_update(id, user_data):
        return "User updated succesfully", 204
    return jsonify({"An error occurred": "Invalid request"}), 400


@app.put("/users/<id:int>")
def user_replace(id):
    user_data = request.get_json()
    if controller.user_update(id, user_data):
        return "User repleaced succesfully", 204
    return jsonify({"An error occurred": "Invalid request"}), 400


@app.delete("/users/<int:id>")
def user_delete(id):
    if controller.user_delete(id):
        return "User deleted succesfully", 204
    return jsonify({"An error occurred": "User not found"}), 400


if __name__ == "__main__":
    app.run()
