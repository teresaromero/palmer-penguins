import streamlit as st
from utils.constants import NAVIGATION, NAV_VIZ
from pages.data_visualization import sidebar_filter


def navbar():
    st.subheader("Navigation")
    st.radio("Go to...", options=NAVIGATION, key="page")

def show_sidebar():
    sidebar = st.sidebar
    with sidebar:
        navbar()
        if st.session_state.page == NAV_VIZ:
            sidebar_filter()
