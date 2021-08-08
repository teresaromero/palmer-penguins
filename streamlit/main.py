from pages.home import show_home
from pages.histograms import show_histograms
from utils.main import inizialize_dataframe, menu_selector
import streamlit as st


inizialize_dataframe()


sidebar = st.sidebar
with sidebar:
    menu_selector()


page = st.session_state["page"]
if page == "Histograms":
    show_histograms(sidebar)
if page == "Datasets":
    show_datasets()
else:
    show_home()
