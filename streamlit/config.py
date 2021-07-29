import os
from dotenv import load_dotenv
load_dotenv()


API_URL = os.getenv("API_URL") if os.getenv(
    "API_URL") else "http://localhost:5000"
