from datetime import datetime
from flask import jsonify, request
from models.counsellor import Counsellor
from utils.database import get_counsellor_collection

def create_counsellor():
    data = request.get_json()

    counsellor_collection = get_counsellor_collection()
    counsellor = Counsellor(
        _id=data["_id"],
        name=data["name"],
        specialization=data["specialization"],
        experience=data["experience"],
        num_sessions=data["num_sessions"],
        about=data["about"],
        contact=data["contact"],
        availability=data["availability"],
        qualifications=data["qualifications"],
        ratings=data["ratings"],
        reviews=data["reviews"],
        created_at=datetime.now(),
        updated_at=datetime.now(),
        profile_picture=data["profile_picture"],
    )

    result = counsellor_collection.insert_one(counsellor.__dict__)
    if result.acknowledged:
        return jsonify({"message": "Counsellor created successfully"}), 201
    else:
        return jsonify({"message": "Something went wrong. Failed to create counsellor"}), 500

def get_counsellor(counsellor_id):
    counsellor_collection = get_counsellor_collection()
    counsellor = counsellor_collection.find_one({"_id": counsellor_id})

    if counsellor:
        return jsonify(counsellor), 200
    else:
        return jsonify({"message": "Counsellor not found"}), 404

def get_counsellors():
    counsellor_collection = get_counsellor_collection()
    counsellors = counsellor_collection.find()

    if counsellors:
        return jsonify(list(counsellors)), 200
    else:
        return jsonify({"message": "Counsellors not found"}), 404

def update_counsellor(counsellor_id):
    data = request.get_json()

    updated_counsellor = {
        "name": data.get("name"),
        "specialization": data.get("specialization"),
        "experience": data.get("experience"),
        "num_sessions": data.get("num_sessions"),
        "about": data.get("about"),
        "contact": data.get("contact"),
        "availability": data.get("availability"),
        "qualifications": data.get("qualifications"),
        "ratings": data.get("ratings"),
        "reviews": data.get("reviews"),
        "updated_at": datetime.now(),
        "profile_picture": data.get("profile_picture"),
    }

    counsellor_collection = get_counsellor_collection()
    result = counsellor_collection.update_one(
        {"_id": counsellor_id},
        {"$set": updated_counsellor},
    )

    if result.modified_count > 0:
        return jsonify({"message": "Counsellor updated successfully"}), 200
    else:
        return jsonify({"message": "Something went wrong. Failed to update counsellor"}), 500
    
def delete_counsellor(counsellor_id):
    counsellor_collection = get_counsellor_collection()
    result = counsellor_collection.delete_one({"_id": counsellor_id})

    if result.deleted_count > 0:
        return jsonify({"message": "Counsellor deleted successfully"}), 200
    else:
        return jsonify({"message": "Counsellor not found"}), 404