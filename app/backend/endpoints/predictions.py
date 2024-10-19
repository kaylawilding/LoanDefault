from fastapi import APIRouter, HTTPException, UploadFile, File, BackgroundTasks
import pickle
import numpy as np
import json
import pandas as pd
import uuid
from sklearn.metrics import accuracy_score
from .dependencies.transform import transform_data
from typing import Any


#instatntiate router
router = APIRouter()

@router.post("/predict")
def Predict(InputFile: UploadFile = File(...)) -> Any:
    """
    Predict the loan default status
    """
    # Convert the data to a pandas dataframe
    df = pd.read_csv(InputFile.file)
    # Transform the data
    df = transform_data(df)
    # Get the model

    with open('./endpoints/dependencies/logreg_model.pickle', 'rb') as f:
        model = pickle.load(f)
    # Get the predictions
    predictions = model.predict(df)
    # # Get the metric
    # metric = 'accuracy'
    # metric_value = accuracy_score(df['target'], predictions)
    # # Create a unique id for the prediction
    # runid = uuid.uuid1()
    # # Create a prediction object
    # prediction = predictions(runid = runid, model_name = 'xgboost', metric = metric, metric_value = metric_value)

    #create json object to return the predictions
    predictions = json.dumps(predictions.tolist())

    return predictions
    



