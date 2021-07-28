

from datetime import datetime
from pandas.core.frame import DataFrame
from database.client import open_db_connection, close_db_connection


def parse_date(date: str):
    return datetime.strptime(date, '%m/%d/%y')


def parse_column_name(column: str):
    return column.split("(")[0].strip().replace(" ", "_").lower()


def parse_boolean(string: str):
    return True if string == "Yes" else False if string == "No" else None


def clean_dataframe(dataframe: DataFrame):
    dataframe["Date Egg"] = dataframe["Date Egg"].apply(
        lambda x: parse_date(x))

    dataframe = dataframe.drop("Comments", 1)

    dataframe = dataframe.rename(columns=lambda x: parse_column_name(x))

    dataframe["clutch_completion"] = dataframe["clutch_completion"].apply(
        lambda x: parse_boolean(x))

    return dataframe


def save_dataframe_to_database(dataframe: DataFrame):
    documents = dataframe.to_dict("records")

    db_client = open_db_connection()
    db = db_client["palmer-penguins"]
    collection = db["kaggle-penguins-lter"]
    collection.drop()
    try:
        result = collection.insert_many(documents)
        print(
            f"🤩 Seed data Success: {len(result.inserted_ids)} documents added to database")
        close_db_connection(db_client)

    except Exception as e:
        print(f"👹 Seed Data Error: {str(e)}")
