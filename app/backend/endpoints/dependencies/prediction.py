import pickle
import json
import pandas as pd
import os

MODEL_FILE = os.getenv('MODEL_FILENAME')

def prediction(df: pd.DataFrame) -> json:
    """
    Predict the loan default status
    """
    # Get the model
    with open(f'./{MODEL_FILE}', 'rb') as f:
        model = pickle.load(f)
    # Get the predictions
    predictions = model.predict(df)
    #create json object to return the predictions
    predictions = json.dumps(predictions.tolist())
    return predictions
