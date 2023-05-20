import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')
USER_COLLECTION_NAME = os.getenv('USERS_COLLECTION')
JOURNAL_COLLECTION_NAME = os.getenv('JOURNAL_COLLECTION')
COUNSELLOR_COLLECTION_NAME = os.getenv('COUNSELLOR_COLLECTION')
APPOINTMENT_COLLECTION_NAME = os.getenv("APPOINTMENT_COLLECTION")

client = MongoClient(MONGODO_URI)

db = client[DATABASE_NAME]

def get_user_collection():
    return db[USER_COLLECTION_NAME]

def get_journal_collection():
    return db[JOURNAL_COLLECTION_NAME]

def get_counsellor_collection():
    return db[COUNSELLOR_COLLECTION_NAME]

def get_appointments_collection():
    return db[APPOINTMENT_COLLECTION_NAME]