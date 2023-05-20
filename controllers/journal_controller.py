from datetime import datetime, timedelta
from flask import jsonify, request
from models.journal import JournalEntry
from utils.database import get_journal_collection
from tensorflow_model import predict_journal_mood


def create_journal_entry(user_id):
    data = request.get_json()

    journal_collection = get_journal_collection()
    journal_entry = JournalEntry(
        date=data["date"],
        description=data["description"],
        mood_value=data["mood_value"],
        mood_score=predict_journal_mood(data["description"]),
    )

    result = journal_collection.update_one(
        # TODO: Insert only if date doesn't exist else update
        {"_id": user_id, },
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


def get_journal_for_mood_graph(user_id):
    jourrnal_collection = get_journal_collection()
    print(user_id);

    today = datetime.now()
    last_week = today - timedelta(days=7)

    query = {
        "_id": user_id,
        "journal_entries.date": {
            "$gte": last_week, #.strftime("%Y-%m-%d"),  # last week
            "$lte": today #.strftime("%Y-%m-%d"),  # today
        },
    }

    result = jourrnal_collection.find_one(query)

    if result is not None:
        journal_entries = result["journal_entries"]
        mood_graph_scores = []

        for entry in journal_entries:
            day_of_week = entry["date"].strftime("%a")
            mood_score = entry["mood_score"]
            mood_graph_scores.append({"day": day_of_week, "mood_score": mood_score})
        
        return jsonify(mood_graph_scores), 200
    else:
        return jsonify({"message": "Journal entries not found"}), 404




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
