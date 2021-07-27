from flask_pymongo import PyMongo
from app import app
import os

mongo = PyMongo(app, serverSelectionTimeoutMS=1000)
try:
    mongo.db.command('ping')
    app.logger.info("MongoDB connexion successful")
except Exception as e:
    app.logger.error(str(e))
    os._exit(1)


def collection(name): return mongo.db[name]


penguins_collection = collection("kaggle-penguins-lter")
