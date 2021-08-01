from json import dumps
from pandas.io import json
import streamlit as st
import pandas as pd
from api.individuals import fetch_all


def show():
    st.header("📊 Individuals description")
    st.subheader("This is a subheader")
    data = fetch_all()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
        st.table(df.describe())
    else:
        st.error("Oops! Seems we are having trouble fetching the info")
