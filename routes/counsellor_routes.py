from flask import Blueprint
from controllers.counsellor_controller import create_counsellor, get_counsellor, get_counsellors, update_counsellor, delete_counsellor

counsellor_routes = Blueprint("counsellor_routes", __name__)

@counsellor_routes.route("/counsellors", methods=["POST"])
def create_counsellors():
    return create_counsellor()

@counsellor_routes.route("/counsellors", methods=["GET"])
def get_all_counsellors():
    return get_counsellors()

@counsellor_routes.route("/counsellors/<counsellor_id>", methods=["GET"])
def get_counsellor_by_id(counsellor_id):
    return get_counsellor(counsellor_id)

@counsellor_routes.route("/counsellors/<counsellor_id>", methods=["PUT"])
def update_counsellor_by_id(counsellor_id):
    return update_counsellor(counsellor_id)

@counsellor_routes.route("/counsellors/<counsellor_id>", methods=["DELETE"])
def delete_counsellor_by_id(counsellor_id):
    return delete_counsellor(counsellor_id)
