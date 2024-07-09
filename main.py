import logging
from fastapi import FastAPI

app = FastAPI()


# SETUP LOGGER
logger = logging.getLogger(__file__)


# DNA
app = FastAPI(
    title='Kaggle API',
    description='Kaggle API',
    version='0.0.1',
    docs_url='/v1/documentation',
    redoc_url='/v1/redoc',
    openapi_url='/v1/openapi.json'
)


@app.get("/")
async def root():
    return {"message": "Hello Kaggle!"}

