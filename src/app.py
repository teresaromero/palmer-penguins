from flask import Flask
from config import MONGO_DBNAME, MONGO_URI

app = Flask("palmer-penguins-api")

app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = MONGO_URI
