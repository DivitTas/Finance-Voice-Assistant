from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Finance Voice Assistant API"}