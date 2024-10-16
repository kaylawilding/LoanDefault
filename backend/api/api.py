from fastapi import FastAPI
from .endpoints import predictions

#Instatntiate the router
api_router = FastAPI()

#Add the predictions router to the api router
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])

