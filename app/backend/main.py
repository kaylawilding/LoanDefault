from fastapi import FastAPI
from .endpoints import predictions

#Instatntiate the router
app = FastAPI()

#Add the predictions router to the api router
app.include_router(predictions.router, prefix="/predictions", tags=["predictions"])

