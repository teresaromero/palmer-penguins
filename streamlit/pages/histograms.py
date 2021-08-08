
from components.species import dist_prop_by_species
from utils.main import get_filter, filter_dt
import streamlit as st


def show_histograms(sidebar):
    dataframe = st.session_state.dataframe
    with sidebar:
        st.subheader("Filters")
        filter_fields = ['sex', 'name_species', 'name_island']
        for f in filter_fields:
            filter_keys = get_filter(dataframe, f)
            st.radio(f.replace("_", " ").title(), filter_keys,
                     key=f)

    applied_filters = [st.session_state[s]
                       for s in st.session_state.keys() if s in filter_fields]
    filtered_dt = filter_dt(dataframe, applied_filters)
    if filtered_dt.empty:
        st.warning("Sorry, your filtering does not match with any data")
    else:
        dist_fields = ['body_mass', 'culmen_length',
                       'culmen_depth', 'flipper_length']
        for f in dist_fields:
            dist_prop_by_species(filtered_dt, f)
