from pages.datasets import show_datasets
from pages.home import show_home
from pages.histograms import show_histograms
from utils.main import inizialize_dataframe, menu_selector
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
    menu_selector()


page = st.session_state["page"]
if page == "Histograms":
    show_histograms(sidebar)
if page == "Datasets":
    show_datasets()
if page == "Home":
    show_home()
