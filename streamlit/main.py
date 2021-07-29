from data.requests import get_all_penguins
import streamlit as st
import pandas as pd

header = st.beta_container()
motivation = st.beta_container()
description = st.beta_container()
data = st.beta_container()
fetch_all_data = st.beta_container()
display_data = st.beta_container()

all_data = []

df = pd.DataFrame()

with header:
    st.title("🐧 Palmer Penguins Data Project")

with motivation:
    st.header("👩🏼‍💻 Motivation")
    st.subheader("This is a subheader")
    '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sagittis varius sem, sit amet vehicula dolor pulvinar in. In consequat tincidunt metus id tincidunt. Quisque auctor ipsum quam. Aenean vulputate elit libero, eget ullamcorper nisi sagittis sit amet. Aenean gravida justo et gravida ultricies. Maecenas feugiat justo auctor odio accumsan, ut maximus lacus scelerisque. Sed sit amet velit odio. Aenean ut lectus consequat, cursus nulla ut, lobortis lectus. Integer luctus molestie orci non finibus. Praesent euismod cursus est, consequat sodales metus blandit quis. Ut suscipit feugiat nunc eu fringilla. Nam sit amet condimentum tellus. Nunc varius metus lobortis, feugiat eros eget, scelerisque dui. Nunc bibendum felis eget imperdiet malesuada.
    '''
with description:
    st.header("📃 Description")
    st.subheader("This is a subheader")
    '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sagittis varius sem, sit amet vehicula dolor pulvinar in. In consequat tincidunt metus id tincidunt. Quisque auctor ipsum quam. Aenean vulputate elit libero, eget ullamcorper nisi sagittis sit amet. Aenean gravida justo et gravida ultricies. Maecenas feugiat justo auctor odio accumsan, ut maximus lacus scelerisque. Sed sit amet velit odio. Aenean ut lectus consequat, cursus nulla ut, lobortis lectus. Integer luctus molestie orci non finibus. Praesent euismod cursus est, consequat sodales metus blandit quis. Ut suscipit feugiat nunc eu fringilla. Nam sit amet condimentum tellus. Nunc varius metus lobortis, feugiat eros eget, scelerisque dui. Nunc bibendum felis eget imperdiet malesuada.
    '''
with data:
    st.header("📊 Data Analysis")
    st.subheader("This is a subheader")
    '''
    In order to retrieve the data for the first time, please click Get Data.
    '''
    with fetch_all_data:
        get_data = st.button("Get All Data")
        if get_data:
            with st.spinner("Fetching data from API"):
                all_data = get_all_penguins()
            st.balloons()

    with display_data:
        if len(all_data) != 0:
            df = df.append(all_data)
            st.write('Total records:', len(all_data))
