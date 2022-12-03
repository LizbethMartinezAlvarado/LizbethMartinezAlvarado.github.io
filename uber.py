import streamlit as st
import pandas as pd

uber_data = 'uber-raw-data-sep14.csv'
date_column = 'Date/Time'

@st.cache
def load_data(n_rows):
    data = pd.read_csv(uber_data, nrows = n_rows)
    lowercase = lambda x: str(x).lower()
    data[date_column] = pd.to_datetime(data[date_column])
    data.rename(lowercase, axis = 'columns', inplace = True)
    return data

data = load_data