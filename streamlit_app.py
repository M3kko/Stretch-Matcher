import streamlit as st

# Title of the Streamlit app
st.title("Fitness Stretch Recommendation App")

# Description
st.write("This app recommends stretches based on different attributes like muscle group, difficulty, and type.")

# Define the dataset
stretches = [
    # Dataset here...
    # Copy and paste the dataset from before
]

# Example: Displaying the dataset as a table
if st.button('Show Stretches'):
    for stretch in stretches:
        st.write(stretch)

# Further code for matching algorithm and other functionalities will go here...
