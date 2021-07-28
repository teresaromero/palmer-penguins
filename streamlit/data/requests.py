from config import API_URL
import requests
import streamlit as st


@st.cache
def get_all_penguins():
    data = []
    path = "/penguins"

    while path:
        response = requests.get(f"{API_URL}{path}")
        if response.status_code == 200:
            res = response.json()
            path = res["_page"]["next"]
            data += res["data"]
    return data
