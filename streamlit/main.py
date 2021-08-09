from utils.main import inizialize_dataframe
from components.sidebar import show_sidebar
from pages.datasets import show_datasets
from pages.home import show_home
from pages.data_visualization import show_data_visualization
from utils.constants import NAV_HOME, NAV_DATA, NAV_VIZ
import streamlit as st

st.set_page_config(
    page_icon="🐧",
    page_title="Palmer Archipelago Data Study",
    layout="wide",
    initial_sidebar_state="expanded"
)

inizialize_dataframe()
show_sidebar()
page = st.session_state["page"]

if page == NAV_VIZ:
    show_data_visualization()
if page == NAV_DATA:
    show_datasets()
if page == NAV_HOME:
    show_home()
