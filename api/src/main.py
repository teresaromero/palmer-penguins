from app import app
from config import API_PORT, FLASK_DEBUG
import individuals.routes

app.run("0.0.0.0", debug=FLASK_DEBUG, port=API_PORT)
