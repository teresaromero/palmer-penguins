from utils.constants import FILTER_FIELDS, PROJECT_DATASET_COLUMNS
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import streamlit as st
import pandas as pd
from api.main import request_api


def parse_oid(dict):
    return dict["$oid"]


def parse_date(dict):
    return dict["$date"]


def fetch_source(name='individuals'):
    return request_api(name)


def parse_bson(bson):
    bson['_id'] = parse_oid(bson['_id'])
    if 'species_id' in bson:
        bson['species_id'] = parse_oid(bson['species_id'])
    if 'island_id' in bson:
        bson['island_id'] = parse_oid(bson['island_id'])
    if 'region_id' in bson:
        bson['region_id'] = parse_oid(bson['region_id'])
    if 'date_egg' in bson:
        bson['date_egg'] = parse_date(bson['date_egg'])
    return bson


def get_dataframe(source: str):
    df = pd.DataFrame()
    try:
        data = fetch_source(source)
        if data:
            df = pd.DataFrame([parse_bson(doc) for doc in data])
        else:
            st.error("Oops! Seems we are having trouble fetching the info")
        return df
    except Exception as e:
        st.error(str(e))


def filter_dataframe(dataframe, filter: dict):
    df_final: DataFrame = dataframe

    for f in FILTER_FIELDS:
        if filter[f] != "ALL":
            df_final = df_final[df_final[f] == filter[f]]

    return df_final

