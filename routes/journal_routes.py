from flask import Blueprint
from controllers.journal_controller import create_journal_entry, get_journal, delete_journal_entry, get_journal_for_mood_graph

journal_routes = Blueprint("journal_routes", __name__)


@journal_routes.route("/users/<user_id>/journal", methods=["POST"])
def create_journal(user_id):
    return create_journal_entry(user_id)


@journal_routes.route("/users/<user_id>/journal", methods=["GET"])
def get_user_journal(user_id):
    return get_journal(user_id)


@journal_routes.route("/users/<user_id>/journal/mood", methods=["GET"])
def get_user_journal_for_mood_graph(user_id):
    return get_journal_for_mood_graph(user_id)


@journal_routes.route("/users/<user_id>/journal/<entry_date>", methods=["DELETE"])
def delete_journal(user_id, entry_date):
    return delete_journal_entry(user_id, entry_date)
