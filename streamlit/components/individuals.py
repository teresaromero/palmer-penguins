from pandas.core.frame import DataFrame
import streamlit as st

hist_fields = ["culmen_length", "culmen_depth",
               "flipper_length", "body_mass"]


def histogram(df_individuals: DataFrame, fields: list[str]):
    st.subheader("All Individuals Histograms")
    for c in fields:
        st.text(c.replace("_", " ").title())
        st.vega_lite_chart(df_individuals, {
            "mark": "bar",
            "encoding": {
                "x": {
                    "bin": True,
                    "field": c
                },
                "y": {"aggregate": "count"}
            }
        }, use_container_width=True)


def sex_dist(df_individuals: DataFrame):
    st.subheader("Individuals Sex Distribution")
    sex_dist = df_individuals["sex"].value_counts().to_dict()
    values = [{"category": v, "value": sex_dist[v]} for v in sex_dist.keys()]
    st.vega_lite_chart(values, {
        "mark": {"type": "arc", "innerRadius": 50},
        "encoding": {
            "theta": {"field": "value", "type": "quantitative"},
            "color": {"field": "category", "type": "nominal"}
        },
        "view": {"stroke": None}

    }, use_container_width=True)
