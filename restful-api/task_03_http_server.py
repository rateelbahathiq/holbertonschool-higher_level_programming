#!/usr/bin/env python3
"""
Simple Flask API for managing users in memory.
Supports adding users, checking status, listing usernames, and retrieving user info.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage using a dictionary
users = {}

# Root route — confirms the server is running
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

# Returns a list of all usernames (keys in the users dictionary)
@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys())), 200

# Simple health-check route
@app.route("/status", methods=["GET"])
def status():
    return "OK", 200

# Returns user info for a given username, or 404 if not found
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404

# Adds a new user from a POSTed JSON body
@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()

    # If the JSON is not valid or empty
    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check that "username" key is provided
    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user["username"]

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the new user in the dictionary
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

# Run the Flask app on port 5000 and listen on all interfaces
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=False)
