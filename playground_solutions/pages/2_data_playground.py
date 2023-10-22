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
st.write(df)

############################################################################
# We can use st.table()

st.subheader("A static table, using st.table()", divider="gray")
st.table(df.head(10))

############################################################################
# We can use st.dataframe

st.subheader("Using st.dataframe()", divider="gray")
st.dataframe(df, use_container_width=True)

############################################################################
# We can configure Pandas styler

st.subheader("Using Styler", divider="gray")
st.dataframe(df.style.background_gradient(subset=["streams"], cmap="BuGn"), use_container_width=True)

############################################################################
# We can make an editable Dataframe

st.subheader("Using st.data_editor()", divider="gray")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

