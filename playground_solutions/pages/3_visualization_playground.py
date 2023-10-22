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
st.scatter_chart(df, x="bpm", y="danceability_%", size="streams", color="mode")

############################################################################
# Altair

st.subheader("Altair", divider="gray")
alt_scatter = alt.Chart(df).mark_circle().encode(
    x="bpm",
    y="danceability_%",
    size="streams",
    color="mode:O",
).interactive()
st.altair_chart(alt_scatter, use_container_width=True)

############################################################################
# Plotly Express

st.subheader("Plotly Express", divider="gray")
px_scatter = px.scatter(
    df,     
    x="bpm",
    y="danceability_%",
    size="streams",
    color="mode",
)
st.plotly_chart(px_scatter, use_container_width=True)

############################################################################
# Seaborn

st.subheader("Seaborn", divider="gray")

f = sns.pairplot(df, vars=["bpm", "streams", "danceability_%"], hue="mode")
st.pyplot(f)

############################################################################
# Matplotlib

st.subheader("Matplotlib", divider="gray")
fig, ax = plt.subplots(figsize=(12, 8))

df.plot.scatter(x="bpm", y="danceability_%", ax=ax)
st.pyplot(fig)

############################################################################

st.header("Part 2: Layout plots", divider="violet")

############################################################################
# Sidebar: put the file upload in the sidebar

############################################################################
# Tabs: take plots into tabs. Show both notations.

############################################################################
# Columns: take plots into columns. Show both notations.
