from fastapi import APIRouter, HTTPException, UploadFile, File, BackgroundTasks
import pickle
import numpy as np
import json
import pandas as pd
import uuid
from sklearn.metrics import accuracy_score
from .dependencies.transform import transform_data
from typing import Any
from .dependencies.prediction import prediction


#instatntiate router
router = APIRouter()

@router.post("/intake_file")
def intake_file(InputFile: UploadFile = File(...)) -> pd.DataFrame:
    """
    Turn file into a pandas dataframe
    """
    # Convert the data to a pandas dataframe
    #Right now assume and support csv files
    df = pd.read_csv(InputFile.file)
    return df

@router.post("/intake_form")
def intake_form(loan_dict: dict) -> pd.DataFrame:
    """
    Turn form dictionary into pandas dataframe
    """
    # Convert the data to a pandas dataframe
    df = pd.DataFrame([loan_dict])
    return df

@router.post("/predict")
def predict(df: pd.DataFrame) -> Any:
    """
    Predict the loan default status
    """
    # Transform the data
    df = transform_data(df)
    predictions = prediction(df)
    return predictions
    



