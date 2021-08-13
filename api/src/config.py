import os
from dotenv import load_dotenv

load_dotenv()

API_PORT = int(os.getenv("API_PORT", 3000))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", 1)
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_APP = os.getenv("FLASK_APP", "palmer-app")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/palmer-penguins")
