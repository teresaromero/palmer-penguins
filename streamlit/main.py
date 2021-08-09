from pages.datasets import show_datasets
from pages.home import show_home
from pages.histograms import show_histograms
from utils.main import inizialize_dataframe
from utils.navigation import navbar, NAV_HOME, NAV_DATA, NAV_VIZ
import streamlit as st

st.set_page_config(
    page_icon="🐧",
    page_title="Palmer Archipelago Data Study",
    layout="wide",
    initial_sidebar_state="expanded"
)

inizialize_dataframe()


sidebar = st.sidebar
with sidebar:
    navbar()


page = st.session_state["page"]
if page == NAV_VIZ:
    show_histograms(sidebar)
if page == NAV_DATA:
    show_datasets()
if page == NAV_HOME:
    show_home()
