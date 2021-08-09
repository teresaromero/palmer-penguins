from datetime import datetime
from pandas.core.frame import DataFrame


def parse_date(date: str):
    return datetime.strptime(date, '%m/%d/%y').isoformat()


def parse_column_name(column: str):
    return column.split("(")[0].strip().replace(" ", "_").lower()


def parse_boolean(string: str):
    return True if string == "Yes" else False if string == "No" else None


def clean_kg_dataframe(dataframe: DataFrame):

    
    dataframe = dataframe.rename(columns=lambda x: parse_column_name(x))

    dataframe["date_egg"] = dataframe["date_egg"].apply(
        lambda d: parse_date(d))

    dataframe = dataframe.drop("comments", 1)

    dataframe["clutch_completion"] = dataframe["clutch_completion"].apply(
        lambda x: parse_boolean(x))

    dataframe = dataframe[(dataframe["sex"] == "FEMALE")
                          | (dataframe["sex"] == "MALE")]

    species_arr = dataframe["species"]
    common_name = []
    scientific_name = []
    for s in species_arr:
        name_arr = s.split("(")
        common_name.append(name_arr[0].replace(")", "").strip().lower())
        scientific_name.append(name_arr[1].replace(")", "").strip().lower())

    dataframe['common_name'] = common_name
    dataframe['scientific_name'] = scientific_name


    dataframe.dropna(inplace=True)

    return dataframe


def save_dataframe_to_file(dataframe: DataFrame, location):
    dataframe.to_json(location, "records")
