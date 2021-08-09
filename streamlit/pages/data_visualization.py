
from utils.constants import MEASURES_DISTRIBUTION, FILTER_FIELDS
from pandas.core.frame import DataFrame
from components.species import dist_prop_by_species
from utils.main import filter_dataframe
import streamlit as st


def sidebar_filter():
    dataframe: DataFrame = st.session_state.dataframe
    st.subheader("Filters")
    fields = FILTER_FIELDS
    for f in fields:
        label = f.replace("_", " ").title()
        options = ("ALL",)+tuple(dataframe[f].unique())
        key = f"{f}_filter"
        st.radio(label, options, key=key)


def get_filter_keys():
    return [f for f in st.session_state if f.endswith("_filter")]


def selected_filters():
    keys = get_filter_keys()
    return {k.replace("_filter", ""): st.session_state[k] for k in keys}


def show_data_visualization():

    filter = selected_filters()

    filtered_dt = filter_dataframe(filter)

    if filtered_dt.empty:
        st.warning("Sorry, your filtering does not match with any data")
    else:
        for f in MEASURES_DISTRIBUTION:
            dist_prop_by_species(filtered_dt, f)

    delta_scatter()


def delta_scatter():
    st.header("δ15N vs. δ13C")
    st.vega_lite_chart(st.session_state.dataframe, {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "mark": "circle",
        "encoding": {
            "x": {"field": "delta_13_c", "type": "quantitative"},
            "y": {"field": "delta_15_n", "type": "quantitative"}
        }
    }, use_container_width=True)
