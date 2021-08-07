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
