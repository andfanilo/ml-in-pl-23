import pandas as pd
import streamlit as st

@st.cache_data
def load_data(raw_file):
    df = pd.read_csv(raw_file, encoding='ISO-8859-1')
    return df

st.title("Spotify data playground")

raw_data = st.file_uploader("Upload CSV file")

if raw_data is None:
    st.warning("Please upload a file")
    st.stop()

df = load_data(raw_data)

############################################################################
# We can use write on the Dataframe

st.subheader("A dataframe written using st.write()", divider="gray")

############################################################################
# We can use st.table()

st.subheader("A static table, using st.table()", divider="gray")

############################################################################
# We can use st.dataframe

st.subheader("Using st.dataframe()", divider="gray")

############################################################################
# We can configure Pandas styler

st.subheader("Using Styler", divider="gray")

############################################################################
# We can make an editable Dataframe

st.subheader("Using st.data_editor()", divider="gray")

