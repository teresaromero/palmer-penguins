import streamlit as st


NAV_HOME = "🏠 Home"
NAV_VIZ = "📊 Data Visualization"
NAV_DATA = "💾 Datasets Source"
NAVIGATION = [NAV_HOME, NAV_VIZ, NAV_DATA]


def navbar():
    st.subheader("Navigation")
    st.radio("Go to...", options=NAVIGATION, key="page")
