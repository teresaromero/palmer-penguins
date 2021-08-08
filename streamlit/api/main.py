from config import API_URL
import requests
import streamlit as st


@st.cache
def request_api(source: str):
    response = requests.get(f"{API_URL}/{source}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


def update_individual(id: str, payload: dict):
    response = requests.patch(
        f"{API_URL}/individuals/{id}", json=payload)
    if response.status_code == 200:
        st.balloons()
        return response.json()
    elif response.status_code == 404 or response.status_code == 400:
        st.warning(response.json()["error"])
        return None
    else:
        st.error(response.json())
        return None
