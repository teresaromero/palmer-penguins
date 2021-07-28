import os
import dotenv

dotenv.load_dotenv()

PORT = os.getenv("PORT") if os.getenv("PORT") else 5000
FLASK_ENV = os.getenv("FLASK_ENV") if os.getenv("FLASK_ENV") else 'development'
MONGO_URI = os.getenv("MONGO_URI") if os.getenv(
    "MONGO_URI") else 'mongodb://localhost:27017'
MONGO_DBNAME = os.getenv("MONGO_DBNAME") if os.getenv(
    "MONGO_DBNAME") else 'palmer-penguins'
