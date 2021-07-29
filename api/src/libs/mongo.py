from time import sleep
from flask_pymongo import PyMongo
from app import app
import os

mongo = None
try:
    mongo = PyMongo(app, serverSelectionTimeoutMS=5000)

    mongo.db.command('ping')
    app.logger.info("MongoDB connexion successful")

except Exception as e:
    app.logger.error(str(e))
    os._exit(1)


def collection(name): return mongo.db[name]


def penguins_collection():
    return collection("kaggle-penguins-lter")
