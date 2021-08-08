import streamlit as st
from pandas.core.frame import DataFrame
from streamlit.elements.arrow import Data


def dist_prop_by_species(df: DataFrame, prop: str):
    title = prop.replace("_", " ").title()
    st.subheader(f"{title} By Species")
    vega_area_chart(df, prop, "name_species", title)


def vega_area_chart(df: Data, prop: str, group: str, title: str):
    st.vega_lite_chart(df, {
        "mark": "area",
        "transform": [
            {
                "density": prop,
                "groupby": [group],
                "extent": [df[prop].min(), df[prop].max()],
            }
        ],
        "encoding": {
            "x": {"field": "value", "type": "quantitative", "title": title},
            "y": {"field": "density", "type": "quantitative"},
            "color": {"field": group, "type": "nominal"}
        }

    }, use_container_width=True)
