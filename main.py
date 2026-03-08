from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "mysecretkey"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

jwt = JWTManager(app)

# In-memory user store (for demo)
USERS = {
    "kartikey": generate_password_hash("kartikey@123")
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
   
    if username not in USERS or not check_password_hash(USERS[username], password):
        return jsonify({"error": "Invalid credentials"}), 401
   
    token = create_access_token(identity=username)
    return jsonify({"token": token}), 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
