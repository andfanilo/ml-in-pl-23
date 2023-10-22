import streamlit as st

# Create a title, header, and subheader
st.title("Welcome ML in PL!")
st.header("Hope you are doing well")
st.subheader("My name is Fanilo 😏")

# Play with some nifty text
st.markdown("""
Hello :fire:
            
Here's a math formulae: $a + ar + a r^2 + a r^3$
            
:red[This is a beautiful red]
""")

st.divider()

# Create a button
my_button = st.button(label="Send balloons :balloon:")

# Add an action to your button - the best action in streamlit
if my_button:
    st.balloons()

st.divider()

# Add a slider that prints slider value
slider_value = st.slider("Slider")
st.write(f"The slider value is: {slider_value}")

st.divider()

# Create an updateable placeholder
counter_placeholder = st.empty()

# Lets try to make a clicker counter! Create an empty placeholder and a button
my_counter = 0
increment_counter = st.button(label="Click to add one!")

# Add the button action
if increment_counter:
    my_counter += 1
    counter_placeholder.write(f"Button clicked {my_counter} time(s)")

# Doesn't work?! What's wrong!

# Use the session state
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

# Recreate the button and assign the action
if increment_counter:
    st.session_state.counter += 1
    counter_placeholder.write(f"Yay button clicked {st.session_state.counter} times!")

st.divider()
