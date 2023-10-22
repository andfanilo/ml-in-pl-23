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

season_selected = st.radio(label=question, options=seasons)
st.write(f"Your favourite season is {season_selected}")

############################################################################

st.subheader("Dropdown / selectbox", divider="gray")
st.caption("You can only pick one")

season_selected_drop_down = st.selectbox(question, options=seasons)
st.write(f"Your favourite season is {season_selected_drop_down}")

############################################################################

st.subheader("Multiselect", divider="gray")
st.caption("You can pick many")

season_selected_multi = st.multiselect(question, options=seasons)
st.write(f"Your favourite seasons are: {season_selected_multi}")

############################################################################

st.subheader("Checkbox", divider="gray")

# Create a dictionary of the labels and the current state
options = {option: None for option in seasons}

# Loop through the dictionary to create the checkbox and write the current value
for option, checkbox in options.items():
    options[option] = st.checkbox(option)

for option, checkbox in options.items():
    if checkbox:
        st.write(f"You like {option}")

############################################################################

st.subheader("Toggle", divider="gray")

# Create a dictionary of the labels and the current state
options = {option: None for option in seasons}

# Loop through the dictionary to create the checkbox and write the current value
for option, checkbox in options.items():
    options[option] = st.toggle(option)

for option, checkbox in options.items():
    if checkbox:
        st.write(f"You like {option}")

############################################################################

st.subheader("Slider", divider="gray")

slider_value = st.slider(
    f"As a %, How much do you love {season_selected}",
    min_value=0,
    max_value=100,
    value=100,
    step=5,
    format="%d%%",
    help="Pick something between 0 and 100",
)

st.write(f"You like {season_selected} {slider_value}%")

############################################################################

st.subheader("Select Slider", divider="gray")

slider_item = st.select_slider(
    label=f"How much do you like {season_selected_drop_down}",
    options=["I don't", "A little", "A lot", "It's the Best!"],
)

st.write(f"You like {season_selected_drop_down} {slider_item.lower()}!")

############################################################################

st.subheader("Text Input", divider="gray")

user_text = st.text_input(label=question)

if user_text:
    st.write(f"You've entered {user_text}")

############################################################################

st.subheader("Number Input", divider="gray")

user_number = st.number_input(
    label=f"As a %, How much do you love {season_selected}",
    min_value=0,
    max_value=100,
    step=10,
)

if user_number:
    st.write(f"I score it {user_number} / 100")

############################################################################

st.subheader("Date Input", divider="gray")

user_date = st.date_input(label=f"When is your birthday?")

st.write(f"My Birthday is {user_date}")

############################################################################

# st.stop() # Comment when you are ready to start this exercise

st.header("Part 2: Putting it together", divider="violet")

raw_data = st.file_uploader("Upload CSV file")

if raw_data is None:
    st.warning("Please upload a file")
    st.stop()
df = pd.read_csv(raw_data, encoding='ISO-8859-1')

############################################################################
# 1. Show dataframe only when toggle is on
# 2. Use a multiselect to hide selected columns
# 3. Use a slider to select rows where streams > X 

preview_data = st.toggle("Preview Dataframe")

if preview_data:
    all_columns = df.columns.values.tolist()
    hide_columns = st.multiselect("Hide columns", all_columns)
    stream_threshold = st.slider(
        "Keep songs with number of streams over:", 
        0, 
        4_000_000_000, 
        1_000_000_000,
        1_000_000,
    )
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
