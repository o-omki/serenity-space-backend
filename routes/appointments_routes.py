from flask import Blueprint, jsonify
from controllers.appointment_controller import create_appointment, update_appointment, delete_appointment, get_appointments_for_counsellor, get_appointments_for_user

appointment_routes = Blueprint("appointment_routes", __name__)

@appointment_routes.route("/appointments", methods=["POST"])
def create_user_appointment():
    return create_appointment()

@appointment_routes.route("/appointments/<appointment_id>", methods=["PUT"])
def get_user_appointment(appointment_id):
    return update_appointment(appointment_id)

@appointment_routes.route("/appointments/<appointment_id>", methods=["DELETE"])
def delete_user_appointment(appointment_id):
    return delete_appointment(appointment_id)

@appointment_routes.route("/counsellors/<counsellor_id>/appointments", methods=["GET"])
def get_counsellor_appointments(counsellor_id):
    return get_appointments_for_counsellor(counsellor_id)

@appointment_routes.route("/users/<user_id>/appointments", methods=["GET"])
def get_user_appointments(user_id):
    return get_appointments_for_user(user_id)
