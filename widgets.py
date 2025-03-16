import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

# Name
name = st.text_input('Enter your name')
# Slider
age = st.slider('Select your age',1,100,25)

# Choice
choise = st.selectbox('Choose',['A','B',1,2,3])

# creating upload button
upload_file = st.file_uploader('Please upload the CSV file')



if name:
    st.write(f"{name} Hello!")
if age:
    st.write(f'Entered age is {age}')
if upload_file:
    df = pd.read_csv(upload_file)
    st.write(df)


