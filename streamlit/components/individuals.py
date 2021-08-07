import streamlit as st
import pandas as pd
from api.individuals import fetch_all
import logging

state = st.session_state

hist_fields = ["culmen_length", "culmen_depth",
               "flipper_length", "body_mass"]


def show():
    st.header("📊 General Data")
    st.subheader("This is a subheader")
    df = pd.DataFrame()

    data = fetch_all()
    if data:
        df = pd.DataFrame(data)
    else:
        logging.error("Error retrieving data from API")
        st.error("Oops! Seems we are having trouble fetching the info")

    st.subheader("Individuals Sex Distribution")
    sex_dist = df["sex"].value_counts().to_dict()
    values = [{"category": v, "value": sex_dist[v]} for v in sex_dist.keys()]
    st.vega_lite_chart(values, {
        "mark": {"type": "arc", "innerRadius": 50},
        "encoding": {
            "theta": {"field": "value", "type": "quantitative"},
            "color": {"field": "category", "type": "nominal"}
        },
        "view": {"stroke": None}

    }, use_container_width=True)

    st.subheader("Data Histogram")
    for c in hist_fields:
        st.vega_lite_chart(df, {
            "mark": "bar",
            "encoding": {
                "x": {
                    "bin": True,
                    "field": c
                },
                "y": {"aggregate": "count"}
            }
        }, use_container_width=True)
