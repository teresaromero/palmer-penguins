from pandas.core.frame import DataFrame
from pandas.core.series import Series
import streamlit as st
import pandas as pd
from api.main import request_api


def parse_oid(series: Series):
    return series.apply(lambda x: x["$oid"])


def fetch_source(name='individuals'):
    return request_api(name)


def get_dataframe(source: str):
    df = pd.DataFrame()
    try:
        data = fetch_source(source)
        if data:
            df = pd.DataFrame(data)
            df['_id'] = parse_oid(df['_id'])
            if 'species_id' in df:
                df['species_id'] = parse_oid(df['species_id'])
            if 'island_id' in df:
                df['island_id'] = parse_oid(df['island_id'])
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
    st.radio("Go to...", ["Home", "Histograms", "Info"], key="page")
