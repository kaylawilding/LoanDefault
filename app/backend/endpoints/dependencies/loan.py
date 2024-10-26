import pandas as pd
import numpy as np
from pydantic import BaseModel
from transform import encode, add_missing_cols


# Properties to receive via API on creation
class Loan(BaseModel):
    Gender: str
    year: str
    loan_amount: int


def create_dataset(loan:Loan) -> pd.DataFrame:
    """
    Creates a dataframe with the class
    """
    # Create a dataframe
    df = pd.DataFrame([loan.dict()])
    # Encode the data
    df_encoded = encode(df)
    #add missing cols
    df_encoded = add_missing_cols(df_encoded)
    # Return the dataframe
    return df_encoded

 

