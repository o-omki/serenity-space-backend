from flask import jsonify, request
from models.journal import JournalEntry
from utils.database import get_journal_collection


def create_journal_entry(user_id):
    data = request.get_json()

    journal_collection = get_journal_collection()
    journal_entry = JournalEntry(
        date=data["date"],
        description=data["description"],
        mood_value=data["mood_value"],
    )

    result = journal_collection.update_one(
        {"_id": user_id},
        {"$push": {"journal_entries": journal_entry.__dict__}},
        upsert=True,
    )

    if result.modified_count > 0:
        return jsonify({"message": "Journal entry created successfully"}), 201
    else:
        return jsonify({"message": "Something went wrong. Failed to create journal entry"}), 500


def get_journal(user_id):
    journal_collection = get_journal_collection()
    journal = journal_collection.find_one({"_id": user_id})

    if journal:
        return jsonify(journal), 200
    else:
        return jsonify({"message": "Journal not found"}), 404


def delete_journal_entry(user_id, entry_date):
    journal_collection = get_journal_collection()
    result = journal_collection.update_one(
        {
            "_id": user_id,

        },
        {
            "$pull": 
            {
                "journal_entries": {"date": entry_date}
            }
        }
    )

    if result.modified_count > 0:
        return jsonify({"message": "Journal entry deleted successfully"}), 200
    else:
        return jsonify({"message": "Journal entry not found"}), 404
