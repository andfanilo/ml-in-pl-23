import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

@st.cache_data
def load_data(raw_file):
    df = pd.read_csv(raw_file, encoding='ISO-8859-1')
    return df

st.title("Spotify data viz playground")

raw_data = st.file_uploader("Upload CSV file")

if raw_data is None:
    st.warning("Please upload a file")
    st.stop()

df = load_data(raw_data)

with st.expander("Data preview"):
    st.dataframe(df.head(15))

st.header("Part 1: Visualize plots", divider="violet")

############################################################################
# Streamlit native charts

st.subheader("Streamlit native chart", divider="gray")

############################################################################
# Altair

st.subheader("Altair", divider="gray")

############################################################################
# Plotly Express

st.subheader("Plotly Express", divider="gray")

############################################################################
# Seaborn

st.subheader("Seaborn", divider="gray")

############################################################################
# Matplotlib

st.subheader("Matplotlib", divider="gray")

############################################################################

st.header("Part 2: Layout plots", divider="violet")

############################################################################
# Sidebar: put the file upload in the sidebar

############################################################################
# Tabs: take plots into tabs. Show both notations.

############################################################################
# Columns: take plots into columns. Show both notations.
