import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title('Uber App')
st.write("Viajes de Uber en la ciudad de Nueva York con filtros por hora.")

url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache
def load_data(norows):
    data = pd.read_csv(url, nrows=norows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(10000)

st.map(data)



