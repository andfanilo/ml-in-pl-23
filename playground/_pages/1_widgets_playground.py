import pandas as pd
import streamlit as st

st.title("Widgets Playground")

st.header("Part 1: Experimenting", divider="violet")

############################################################################
# Set the options and the questions

seasons = ["Spring", "Summer", "Autumn", "Winter"]
question = "What's your favourite season?"

############################################################################

st.subheader("Radio", divider="gray")
st.caption("You can only pick one")

############################################################################

st.subheader("Dropdown / selectbox", divider="gray")
st.caption("You can only pick one")

############################################################################

st.subheader("Multiselect", divider="gray")
st.caption("You can pick many")

############################################################################

st.subheader("Checkbox", divider="gray")

############################################################################

st.subheader("Toggle", divider="gray")

############################################################################

st.subheader("Slider", divider="gray")

############################################################################

st.subheader("Select Slider", divider="gray")

############################################################################

st.subheader("Text Input", divider="gray")

############################################################################

st.subheader("Number Input", divider="gray")

############################################################################

st.subheader("Date Input", divider="gray")

############################################################################

st.stop() # Comment when you are ready to start this exercise

st.header("Part 2: Putting it together", divider="violet")

raw_data = st.file_uploader("Upload CSV file")

if raw_data is None:
    st.warning("Please upload a file")
    st.stop()
df = pd.read_csv(raw_data, encoding='ISO-8859-1')

############################################################################
# Make the following script Streamlit-interactive
# 1. Show dataframe only when toggle is on
# 2. Use a multiselect to hide selected columns
# 3. Use a slider to select rows where streams > X 

preview_data = False

if preview_data:
    all_columns = df.columns.values.tolist()
    hide_columns = "streams"
    stream_threshold = 1_000_000_000
    df = df.loc[
        df["streams"] > stream_threshold, 
        [col for col in all_columns if col not in hide_columns]
    ]
    st.dataframe(df)
    st.download_button(
        label="Download data as CSV",
        data= df.to_csv(),
        file_name='edited_df.csv',
        mime='text/csv',
    )
