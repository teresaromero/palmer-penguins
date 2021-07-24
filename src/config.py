import os
import dotenv

dotenv.load_dotenv()

PORT = os.getenv("PORT")
FLASK_ENV = os.getenv("FLASK_ENV")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
