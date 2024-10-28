from fastapi import APIRouter, HTTPException, UploadFile, File, BackgroundTasks
import pickle
import numpy as np
import json
import pandas as pd
import uuid
from sklearn.metrics import accuracy_score
from .dependencies.transform import transform_data, extra_cols, missings, encode, add_missing_cols
from typing import Any
from .dependencies.prediction import prediction
from models import loandata

#instatntiate router
router = APIRouter()

@router.post("/intake_file")
def intake_file(InputFile: UploadFile = File(...)) -> Any:
    """
    Turn file into a pandas dataframe
    """
    # Convert the data to a pandas dataframe
    #Right now assume and support csv files
    df = pd.read_csv(InputFile.file)
    df = transform_data(df)
    predictions = prediction(df)
    return predictions

@router.post("/intake_form")
def intake_form(loan_data: loandata.LoanData) -> Any:
    """
    Turn form dictionary into pandas dataframe
    """
    # Convert the data to a pandas dataframe
    df = pd.DataFrame([loan_data.dict()])
    df_encoded = encode(df)
    df_complete = add_missing_cols(df_encoded)
    predictions = prediction(df_complete)
    return predictions
    



