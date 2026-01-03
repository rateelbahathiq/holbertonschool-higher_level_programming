#!/usr/bin/python3
"""
Flask API with basic authentication and token-based security.

Features:
- HTTP Basic Authentication using username/password.
- JWT (JSON Web Token) Authentication for protected routes.
- Admin-only access using role-based control.
- Custom error messages for JWT-related issues.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Setup JWT with secret key
app.config['JWT_SECRET_KEY'] = 'Key_2532'
jwt = JWTManager(app)

# Setup Basic Auth
auth = HTTPBasicAuth()

# In-memory user database with hashed passwords and roles
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Verify credentials for Basic Auth
@auth.verify_password
def verify_password(username, password):
    if username in users:
        hashed = users[username]["password"]
        if check_password_hash(hashed, password):
            return users[username]
    return None

# Basic Auth protected route
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Login route to generate JWT token
@app.route('/login', methods=['POST'])
def login_jwt():
    username = request.json.get("username")
    password = request.json.get("password")
    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity={
        "username": username,
        "role": users[username]["role"]
    })
    return jsonify(access_token=access_token)

# JWT-protected route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# JWT-protected route that only allows admin access
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Handle missing token
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

# Handle malformed token
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

# Handle expired token
@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

# Handle revoked token
@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

# Handle fresh token requirement
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# Start the Flask app
if __name__ == "__main__":
    app.run()
