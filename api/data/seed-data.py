
import pandas as pd
import os

from utils.main import clean_dataframe, save_dataframe_to_database
from dotenv import load_dotenv
load_dotenv()


dataframe = pd.read_csv(
    f"{os.path.dirname(os.path.abspath(__file__))}/source/penguins_lter.csv")

final_dataframe = clean_dataframe(dataframe)

save_dataframe_to_database(final_dataframe)
