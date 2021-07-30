import os
from dotenv import load_dotenv
load_dotenv()


API_URL = f"http://{os.getenv('API_HOST')}:{os.getenv('API_PORT')}"
