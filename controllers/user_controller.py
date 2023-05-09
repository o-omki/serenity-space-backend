from datetime import datetime
from flask import jsonify, request
from models.user import User
from utils.database import get_user_collection


def create_user():
    data = request.get_json()

    user_collection = get_user_collection()
    user = User(
        id=data["_id"],
        email=data["email"],
        first_name=data["first_name"],
        middle_name=data["middle_name"],
        last_name=data["last_name"],
        age=data["age"],
        sex=data["sex"],
        address=data["address"],
        profile_picture=data["profile_picture"],
        programme=data["programme"],
        year=data["year"],
        emergency_number=data["emergency_number"],
        created_at=datetime.now(),
        last_active_at=datetime.now()
    )

    result = user_collection.insert_one(user)
    if result.acknowledged:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"message": "Something went wrong. Failed to create user"}), 500


def get_user(user_id):
    user_collection = get_user_collection()
    user = user_collection.find_one({"_id": user_id})

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404


def update_user(user_id):
    data = request.get_json()
    updated_user = {
        "email": data.get("email"),
        "first_name": data.get("first_name"),
        "middle_name": data.get("middle_name"),
        "last_name": data.get("last_name"),
        "age": data.get("age"),
        "sex": data.get("sex"),
        "address": data.get("address"),
        "profile_picture": data.get("profile_picture"),
        "programme": data.get("programme"),
        "year": data.get("year"),
        "emergency_number": data.get("emergency_number"),
        "last_active_at": datetime.now()
    }

    user_collection = get_user_collection()
    result = user_collection.update_one(
        {"_id": user_id}, {"$set": updated_user})

    if result.modified_count > 0:
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404


def delete_user(user_id):
    user_collection = get_user_collection()
    result = user_collection.delete_one({"_id": user_id})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
