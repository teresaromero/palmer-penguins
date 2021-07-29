import os
from dotenv import load_dotenv

load_dotenv()

API_PORT = os.getenv("API_PORT") if os.getenv("API_PORT") else 3000
FLASK_DEBUG = os.getenv("FLASK_DEBUG") if os.getenv("FLASK_DEBUG") else False

MONGO_URI = os.getenv("MONGO_URI") if os.getenv(
    "MONGO_URI") else 'mongodb://mongodb:27017/palmer-penguins'
MONGO_DBNAME = os.getenv("MONGO_DBNAME") if os.getenv(
    "MONGO_DBNAME") else 'palmer-penguins'
