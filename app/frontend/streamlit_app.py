import streamlit as st
import requests


st.title('Loan Default Prediction')

file = st.file_uploader("Upload file", type=["csv"])

if file is not None:
    response = requests.post("https://loandefaultbackend-ayehfjhgd7afgnfv.westus-01.azurewebsites.net/predictions/predict", files={"InputFile": file})
    st.write(response.json())
    predictions = response.json()
    st.write(f"Your loan default predictions are: {predictions}")


gender = st.selectbox(
   'Gender',
    ('Female', 'Male', 'Joint'))

year = st.selectbox(
   'Year',
    ('2010', '2011', '2012', '2013', '2014', 
     '2015', '2016', '2017', '2018', '2019', 
     '2020', '2021', '2022', '2023', '2024'),
     placeholder = "Select Year")

loan_amount = st.number_input('Loan Amount', min_value=0, max_value=10000000, value=0) 
