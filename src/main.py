from app import app
from config import PORT

app.run("0.0.0.0", PORT, debug=True)
