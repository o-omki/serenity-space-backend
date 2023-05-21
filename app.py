from flask import Flask
from routes.user_routes import user_routes
from routes.journal_routes import journal_routes
from routes.counsellor_routes import counsellor_routes
from routes.appointments_routes import appointment_routes
import os
from dotenv import load_dotenv
from tensorflow_model import load_model
import json
from bson.json_util import ObjectId

load_dotenv()
# load_model()

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj) 

app = Flask(__name__)
app.json_encoder = MyEncoder
app.register_blueprint(user_routes, url_prefix="/serenity")
app.register_blueprint(journal_routes, url_prefix="/serenity")
app.register_blueprint(counsellor_routes, url_prefix="/serenity")
app.register_blueprint(appointment_routes, url_prefix="/serenity")

HOST = os.getenv("HOST_IP")

if __name__ == "__main__":
    app.run(debug=True, host=HOST)
