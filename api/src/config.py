import os
from dotenv import load_dotenv

load_dotenv()

API_PORT = int(os.getenv("API_PORT", 3000))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", 1)

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
MONGO_DBNAME = os.getenv("MONGO_DBNAME")

MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}"
