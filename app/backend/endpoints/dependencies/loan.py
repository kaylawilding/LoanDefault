import pandas as pd
import numpy as np
from transform import encode, add_missing_cols

def create_dataset(loan:dict) -> pd.DataFrame:
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

 

