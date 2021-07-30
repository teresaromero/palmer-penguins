from config import API_URL
import requests
import streamlit as st


@st.cache
def get_all_penguins():
    response = requests.get(f"{API_URL}/penguins?page=0")
    if response.status_code == 200:
        return response.json()
    else:
        return {}
    
