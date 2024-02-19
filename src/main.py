
import os
from fastapi import FastAPI
from src.env import config

MODE = config("MODE", cast=str, default='test')

app = FastAPI()

@app.get("/")
def home_page():
    # for API services
    # JSON-ready dict -> json.dumps({'hello': 'world'})
    return {"Hello": "World", "Mode": MODE}





## uvicorn src.main:app