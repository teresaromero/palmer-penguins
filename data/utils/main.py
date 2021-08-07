from datetime import datetime
from pandas.core.frame import DataFrame


def parse_date(date: str):
    return datetime.strptime(date, '%m/%d/%y').isoformat()


def parse_column_name(column: str):
    return column.split("(")[0].strip().replace(" ", "_").lower()


def parse_boolean(string: str):
    return True if string == "Yes" else False if string == "No" else None


def clean_dataframe(dataframe: DataFrame):

    dataframe = dataframe.rename(columns=lambda x: parse_column_name(x))

    dataframe["date_egg"] = dataframe["date_egg"].apply(
        lambda d: parse_date(d))

    dataframe = dataframe.drop("comments", 1)

    dataframe["clutch_completion"] = dataframe["clutch_completion"].apply(
        lambda x: parse_boolean(x))

    dataframe = dataframe[(dataframe["sex"] == "FEMALE")
                          | (dataframe["sex"] == "MALE")]

    return dataframe.dropna()


def save_dataframe_to_file(dataframe: DataFrame):
    dataframe.to_json(
        r'database/docker-entrypoint-initdb.d/seed.json', "records")
