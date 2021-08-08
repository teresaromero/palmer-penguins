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


def get_filter(df: DataFrame, field: str):
    return ("ALL",) + tuple(df[field].unique())


def filter_dt(initial_df: DataFrame, filter_params: list[str]):
    sex_filter, species_filter, island_filter = filter_params
    df_final = initial_df

    if sex_filter != "ALL":
        df_final = df_final[df_final["sex"] == sex_filter]
    if species_filter != "ALL":
        df_final = df_final[df_final["name_species"] == species_filter]
    if island_filter != "ALL":
        df_final = df_final[df_final["name_island"] == island_filter]
    return df_final


def menu_selector():
    st.subheader("Navigation")
    st.radio("Go to...", ["Home", "Datasets",
             "Histograms", "Info"], key="page")


def inizialize_dataframe():
    if 'df_individuals' not in st.session_state:
        st.session_state['df_individuals'] = get_dataframe('individuals')
    if 'df_species' not in st.session_state:
        st.session_state['df_species'] = get_dataframe('species')
    if 'df_islands' not in st.session_state:
        st.session_state['df_islands'] = get_dataframe('islands')
    if 'dataframe' not in st.session_state:
        st.session_state['dataframe'] = st.session_state.df_individuals.merge(
            st.session_state.df_species, left_on='species_id', right_on='_id', suffixes=('_indv', '_species')).merge(
            st.session_state.df_islands, left_on='island_id', right_on='_id', suffixes=('_species', '_island'))
