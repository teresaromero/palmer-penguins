
import pandas as pd
import os

from utils.main import clean_kg_dataframe, save_dataframe_to_file
from dotenv import load_dotenv
load_dotenv()


def get_df(file):
    return pd.read_csv(
        f"{os.path.dirname(os.path.abspath(__file__))}/{file}")


df_kaggle = clean_kg_dataframe(get_df('source/penguins_lter.csv'))

save_dataframe_to_file(
    df_kaggle, r'database/docker-entrypoint-initdb.d/seed.json')

df_species = get_df('scrapper/species.csv')

save_dataframe_to_file(
    df_species, r'database/docker-entrypoint-initdb.d/species.json')
