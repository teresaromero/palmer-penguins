import json
from utils.main import parse_bson
import pandas as pd
from api.main import update_individual
from pandas.core.frame import DataFrame
import streamlit as st


def update_edit():
    id = st.session_state.df_individuals_id
    num_row = int(st.session_state.df_individuals_row)
    payload = {
        "culmen_length": st.session_state.culmen_length_edit,
        "culmen_depth": st.session_state.culmen_depth_edit,
        "flipper_length": st.session_state.flipper_length_edit,
        "body_mass": st.session_state.body_mass_edit,
        "sex": st.session_state.sex_edit
    }
    res = update_individual(id, payload)
    if res:
        df_update = pd.DataFrame(parse_bson(res), index=[num_row])
        st.session_state.df_individuals.loc[num_row] = df_update.loc[num_row]
    clear_row()


def clear_row():
    st.session_state.df_individuals_row = ""
    del st.session_state.df_individuals_id


sex_opts = ["FEMALE", "MALE"]
def sex_value(x): return sex_opts.index(x)


def show_datasets():
    df_individuals: DataFrame = st.session_state.df_individuals
    df_species: DataFrame = st.session_state.df_species
    df_islands: DataFrame = st.session_state.df_islands

    st.header("Individuals Dataset")
    st.dataframe(df_individuals)
    if 'df_individuals_row' not in st.session_state:
        st.session_state.df_individuals_row = ""

    st.text_input(
        "Enter row number to edit", max_chars=3, key="df_individuals_row", value=st.session_state.df_individuals_row)

    if st.session_state.df_individuals_row != "":
        # Column 1 - Search result
        num_row = int(st.session_state.df_individuals_row)
        try:
            row_selected_str = df_individuals.iloc[[num_row]].to_json(
                orient="records")
            row_selected = json.loads(row_selected_str)[0]

            col1, col2 = st.beta_columns(2)
            with col1:
                st.json(row_selected)
            with col2:
                with st.form(key='edit_form', clear_on_submit=True):
                    st.session_state.df_individuals_id = row_selected["_id"]
                    st.number_input(
                        "culmen_length", value=row_selected["culmen_length"],  min_value=0.0, key="culmen_length_edit")
                    st.number_input(
                        "culmen_depth", value=row_selected["culmen_depth"],  min_value=0.0, key="culmen_depth_edit")
                    st.number_input(
                        "flipper_length", value=row_selected["flipper_length"],  min_value=0.0, key="flipper_length_edit")
                    st.number_input(
                        "body_mass", value=row_selected["body_mass"], step=1.0, min_value=0.0, key="body_mass_edit")

                    st.radio(
                        "sex", options=sex_opts, index=sex_value(row_selected["sex"]), key="sex_edit")

                    st.form_submit_button(
                        label="Edit", help="Persist the changes in the database", on_click=update_edit)
                    st.form_submit_button(
                        label="Cancel", help="Exit edit", on_click=clear_row)

        except Exception as e:
            st.error(str(e))

    st.header("Species Dataset")
    st.dataframe(df_species)

    st.header("Islands Dataset")
    st.dataframe(df_islands)
