import streamlit as st
import requests

st.title('Loan Default Prediction')

file = st.file_uploader("Upload file", type=["csv"])

if file is not None:
    response = requests.post("http://backend:8000/predictions/predict", files={"InputFile": file})
    st.write(response.json())
    predictions = response.json()
    st.write(f"Your loan default predictions are: {predictions}")
