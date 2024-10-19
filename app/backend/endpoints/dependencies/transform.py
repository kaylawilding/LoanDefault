import pandas as pd
import numpy as np 
from sklearn.preprocessing import OneHotEncoder
import pickle
from pathlib import Path


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
        Take in the raw input data and transform to a format that can be used by the model

        For now assuming the input file is formatted the same as the training, but to add rules for input later
    """
    loan_df = extra_cols(data)
    loan_df = missings(loan_df)
    loan_df = encode(loan_df)
    loan_df = add_missing_cols(loan_df)
    return loan_df
    

def extra_cols(data: pd.DataFrame) -> pd.DataFrame:
    """
        Function to drop extra columns from the dataset
    """
    loan_df = data.drop(columns=['rate_of_interest', 'Interest_rate_spread', 'Upfront_charges', 'Status', 'ID'])
    return loan_df


def missings(data: pd.DataFrame) -> pd.DataFrame:
    """
        Function to handle missing values in the dataset
    """
    loan_df = data[~data['Gender'].str.contains("Not Available")]
    dict_na = {
        'loan_limit': loan_df['loan_limit'].mode()[0],
        'approv_in_adv': loan_df['approv_in_adv'].mode()[0],
        'loan_purpose': loan_df['loan_purpose'].mode()[0],
        'term': loan_df['term'].mode()[0],
        'Neg_ammortization': loan_df['Neg_ammortization'].mode()[0],
        'property_value': loan_df['property_value'].mean(),
        'income': loan_df['income'].mean(),
        'LTV': loan_df['LTV'].mean(),
        'dtir1': loan_df['dtir1'].mean()
    }
    loan_df = loan_df.fillna(dict_na)
    assert loan_df.isnull().sum().sum() == 0
    return loan_df

def encode(data: pd.DataFrame) -> pd.DataFrame:
    """
        Function to encode the categorical variables in the dataset
    """
    obj_cols = data.select_dtypes(include=['object']).columns.tolist()
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    one_hot_encoded = encoder.fit_transform(data[obj_cols])
    one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(obj_cols))

    data = data.reset_index(drop=True)
    one_hot_df = one_hot_df.reset_index(drop=True)
    # Concatenate the one-hot encoded dataframe with the dataframe
    df_encoded = pd.concat([data, one_hot_df], axis=1)

    # Drop the original categorical columns
    df_encoded = df_encoded.drop(obj_cols, axis=1)

    return df_encoded

def add_missing_cols(data: pd.DataFrame) -> pd.DataFrame:
    """
        Add missing columns to the dataframe
    """
    #load the model
    model_path = Path(__file__).parent / 'logreg_model.pickle'
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    for col in model.feature_names_in_:
        if col not in data.columns:
            data[col] = 0
    data = data[model.feature_names_in_]
    return data
