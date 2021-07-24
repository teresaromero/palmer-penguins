import os
import dotenv

dotenv.load_dotenv()

PORT = os.getenv("PORT")
FLASK_ENV = os.getenv("FLASK_ENV")
