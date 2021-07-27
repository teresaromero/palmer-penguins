from app import app
from config import PORT
import routes.penguins

app.run("0.0.0.0", PORT, debug=True)
