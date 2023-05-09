from flask import Flask
from routes.user_routes import user_routes
from routes.journal_routes import journal_routes
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix="/serenity")
app.register_blueprint(journal_routes, url_prefix="/serenity")

HOST = os.getenv("HOST_IP")

if __name__ == "__main__":
    app.run(debug=True, host=HOST)
