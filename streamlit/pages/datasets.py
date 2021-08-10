import json
from utils.constants import NAV_DATA
from utils.main import get_dataframe
from api.main import update_source
from pandas.core.frame import DataFrame
import streamlit as st
from streamlit import caching


def get_payload(collection):
    if collection == "individuals":
        return individuals_payload()
    elif collection == "species":
        return species_payload()
    elif collection == "islands":
        return islands_payload()


def individuals_payload():
    return {
        "culmen_length": st.session_state.culmen_length_edit,
        "culmen_depth": st.session_state.culmen_depth_edit,
        "flipper_length": st.session_state.flipper_length_edit,
        "body_mass": st.session_state.body_mass_edit,
        "sex": st.session_state.sex_edit
    }


def species_payload():
    return {
        "name": st.session_state.species_name_edit
    }


def islands_payload():
    return {
        "name": st.session_state.islands_name_edit
    }


def update_edit(collection: str, row_index, id_edit):
    payload = get_payload(collection)
    res = update_source(collection.lower(), id_edit, payload)
    if res:
        caching.clear_cache()
        clear_row()

    st.session_state.page == NAV_DATA

def clear_row():
    del st.session_state.row_index


sex_opts = ["FEMALE", "MALE"]
def sex_value(x): return sex_opts.index(x)


def edit_datasets():
    st.header("Edit Datasets")
    st.radio("Choose the dataset to edit:", [
             "Individuals", "Species", "Islands"], key="collection_edit")

    if "row_index" not in st.session_state:
        st.session_state["row_index"] = ""

    st.text_input(
        "Enter row number to edit", max_chars=3, key="row_index", value=st.session_state.row_index)

    if st.session_state.row_index != "":
        # Column 1 - Search result
        row_index = int(st.session_state.row_index)
        collection = st.session_state.collection_edit.lower()
        try:
            df = get_dataframe(collection)
            row_selected_str = df.iloc[[row_index]].to_json(
                orient="records")
            row_selected = json.loads(row_selected_str)[0]

            col1, col2 = st.beta_columns(2)
            with col1:
                st.json(row_selected)
            with col2:
                edit_form(collection, row_index, row_selected)

        except Exception as e:
            st.error(str(e))


def show_datasets():
    df_individuals: DataFrame = get_dataframe('individuals')
    df_species: DataFrame = get_dataframe('species')
    df_islands: DataFrame = get_dataframe('islands')

    st.header("Raw Datasets")

    st.subheader("Individuals Dataset")
    st.dataframe(df_individuals)

    st.subheader("Species Dataset")
    st.dataframe(df_species)

    st.subheader("Islands Dataset")
    st.dataframe(df_islands)

    edit_datasets()


def edit_form(collection, row_index, row_selected):
    with st.form(key='edit_form', clear_on_submit=True):
        id_edit = row_selected["_id"]
        if collection == "individuals":
            individuals_edit_form(row_selected)
        elif collection == "species":
            species_edit_form(row_selected)
        elif collection == 'islands':
            islands_edit_form(row_selected)

        st.form_submit_button(
            label="Edit", help="Persist the changes in the database", on_click=update_edit, args=(collection, row_index, id_edit))
        st.form_submit_button(
            label="Cancel", help="Exit edit", on_click=clear_row)


def individuals_edit_form(row_selected):
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


def species_edit_form(row_selected):
    st.text_input(
        "name", value=row_selected["name"], key="species_name_edit")


def islands_edit_form(row_selected):
    st.text_input(
        "name", value=row_selected["name"], key="islands_name_edit")
