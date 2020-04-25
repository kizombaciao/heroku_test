# https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2

import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Ciao!")

# cache ensures that the data is only downloaded once.
@st.cache
def get_data():
    url = "http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2020-04-16/visualisations/listings.csv"
    return pd.read_csv(url)

df = get_data()

# to display the dataframe on web
st.dataframe(df.head())

# to render the code snippet
st.code("""
@st.cache
def get_data():
    url = "http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2020-04-16/visualisations/listings.csv"
    return pd.read_csv(url)
""", language="python")

# st.echo
# renders and executes

