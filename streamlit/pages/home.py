import streamlit as st
import os
from PIL import Image


def show_home():
    st.title("🐧 Palmer Archipelago Penguins")
    st.header("A Data Project by Teresa Romero")
    st.subheader("August, 2021")

    st.markdown("""
    ---
    """)

    image = Image.open(os.path.dirname(__file__)+'/assets/penguins.jpeg')
    st.image(image, caption='Emperor Penguins, Gould Bay, Antarctica (16437100992).jpg - Author: Christopher Michel from San Francisco, USA')

    st.markdown("""

    The purpose for this project is to consolidate all the learned in the Data Bootcamp in [Core Code School](https://www.corecode.school/bootcamp/big-data-machine-learning).

    Objective was to create a simple Streamlit dashboard, having a base csv dataset, creating an API in Flask to serve the data, that is stored in a database.

    All data displayed in this project is coming from the following sources:

    - [Kaggle Dataset](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data)
    - [National Geographic](https://www.nationalgeographic.com)

    You can read more on the project [here](https://github.com/teresaromero/palmer-penguins).


    Coded with 💖 by Tere.
    """)
