import streamlit as st
import requests
import os

BACKEND_URL = os.getenv('BACKEND_URL')

st.title('Loan Default Prediction')
st.write('Please either upload a CSV file or fill out the form below to get your loan default predictions.')

st.write('## Upload CSV File')
file = st.file_uploader("Upload file", type=["csv"])

if file is not None:
    df = requests.post(f"{BACKEND_URL}/predictions/intake_csv", files={"InputFile": file})
    response = requests.post(f"{BACKEND_URL}/predictions/predict", df=df)
    st.write(f"Your loan default predictions are: {response.json()}")

## Form Option
st.write('## Fill out the form')
with st.form('LoanApp'):
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
    submit_for_prediction = st.form_submit_button("Submit")
    if submit_for_prediction:
        loan_dict = {
            'Gender': gender,
            'year': year,
            'loan_amount': loan_amount
        }
        df = requests.post(f"{BACKEND_URL}/predictions/intake_form", loan_dict=loan_dict)
        response = requests.post(f"{BACKEND_URL}/predictions/predict", df=df)
        st.write(f"Your loan default predictions are: {response.json()}")

