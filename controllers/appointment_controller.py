from datetime import datetime
from flask import jsonify, request
from models.appointment import Appointment
from utils.database import get_appointments_collection
from bson import ObjectId
from models.appointment import Appointment
from pymongo import collection


def create_appointment():
    data = request.get_json()

    appointment_collection = get_appointments_collection()
    appointment = Appointment(
        _id=None,
        user_id=data["user_id"],
        user_name=data["user_name"],
        user_picture=data["user_picture"],
        confirmed=data["confirmed"],
        status=data["status"],
        appointment_date=data["appointment_date"],
        description=data["description"],
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        counsellor_id=str(data["counsellor_id"]),
        counsellor_name=data["counsellor_name"],
        counsellor_picture=data["counsellor_picture"]
    )

    result = appointment_collection.insert_one(appointment.dict())
    if result.acknowledged:
        return jsonify({"message": "Appointment created successfully"}), 201
    else:
        return jsonify({"message": "Something went wrong. Failed to create appointment"}), 500


def update_appointment(appointment_id):
    data = request.get_json()
    updated_appointment = {
        "user_id": data.get("user_id"),
        "user_name": data.get("user_name"),
        "user_picture": data.get("user_picture"),
        "confirmed": data.get("confirmed"),
        "status": data.get("status"),
        "appointment_date": data.get("appointment_date"),
        "description": data.get("description"),
        "updated_at": datetime.now().isoformat(),
        "counsellor_id": str(data.get("counsellor_id")),
        "counsellor_name": data.get("counsellor_name"),
        "counsellor_picture": data.get("counsellor_picture")
    }

    appointment_collection = get_appointments_collection()
    result = appointment_collection.update_one(
        {"_id": ObjectId(appointment_id)}, {"$set": updated_appointment}, upsert=False
    )

    if result.modified_count > 0:
        return jsonify({"message": "Appointment updated successfully"}), 200
    else:
        return jsonify({"message": "Appointment not found"}), 404


def delete_appointment(appointment_id):
    appointment_collection = get_appointments_collection()
    result = appointment_collection.delete_one(
        {"_id": ObjectId(appointment_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Appointment deleted successfully"}), 200
    else:
        return jsonify({"message": "Appointment not found"}), 404


def get_appointments_for_counsellor(counsellor_id):
    appointment_collection = get_appointments_collection()
    appointments = appointment_collection.find(
        {"counsellor_id": str(counsellor_id)})
    return jsonify(list(appointments)), 200


def get_appointments_for_user(user_id):
    appointment_collection = get_appointments_collection()
    appointments = appointment_collection.find({"user_id": user_id})
    return jsonify(list(appointments)), 200
