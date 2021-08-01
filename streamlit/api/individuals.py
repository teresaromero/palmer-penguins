from config import API_URL
import requests
import streamlit as st


@st.cache
def fetch_all():
    response = requests.get(f"{API_URL}/individuals")
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
