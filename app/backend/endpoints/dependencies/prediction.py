import pickle
import json
import pandas as pd
import os
from typing import Any
from pathlib import Path

MODEL_FILE = os.getenv('MODEL_FILENAME')

def prediction(df: pd.DataFrame) -> Any:
    """
    Predict the loan default status
    """
    # Get the model
    model_path = Path(__file__).parent / 'logreg_model.pickle'
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    # Get the predictions
    predictions = model.predict(df)
    #create json object to return the predictions
    predictions = json.dumps(predictions.tolist())
    return predictions
