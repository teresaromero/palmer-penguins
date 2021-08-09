import streamlit as st
from pandas.core.frame import DataFrame


def show_species():
    df: DataFrame = st.session_state.df_species
    st.header("Meet the peeps!")
    st.subheader(
        "These are the basic data from the species on the data of this project")
    st.markdown("""
        ---
        """)
    rows, _ = df.shape
    columns = df.columns[1:]
    for r in range(rows):
        for c in columns:
            column_name = c.replace("_", " ").title()
            st.text(f"{column_name}: {df.loc[r][c]}")
        st.markdown("""
        ---
        """)
