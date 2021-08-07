from pages.home import show_home
from pages.histograms import show_histograms
from utils.main import get_dataframe, menu_selector
import streamlit as st


df_individuals = get_dataframe('individuals')
df_species = get_dataframe('species')
df_islands = get_dataframe('islands')

dataframe = df_individuals.merge(
    df_species, left_on='species_id', right_on='_id', suffixes=('_indv', '_species')).merge(
    df_islands, left_on='island_id', right_on='_id', suffixes=('_species', '_island'))

sidebar = st.sidebar
with sidebar:
    menu_selector()


page = st.session_state["page"]
if page == "Histograms":
    show_histograms(dataframe, sidebar)
else:
    show_home()
