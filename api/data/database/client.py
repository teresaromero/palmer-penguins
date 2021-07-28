from pymongo import MongoClient
import os


def open_db_connection():
    try:
        MONGO_URL = os.getenv("MONGO_URL") if os.getenv(
            "MONGO_URL") else "mongodb://localhost:27017/palmer-penguins"

        client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=3000)
        print(
            f"🤩 DB Connection Open")
        return client
    except Exception as e:
        print(f"👹 DB Connection Error: {str(e)}")
        os.abort()


def close_db_connection(client: MongoClient):
    client.close()
    print(
        f"🤩 DB Connection Closed")
