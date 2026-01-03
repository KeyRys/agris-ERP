import psycopg2
from dotenv import load_dotenv
import os

from fastapi import FastAPI

# Load environment variables from .env
load_dotenv()

app = FastAPI(
    title="Agris ERP",
    description="Agribusiness ERP with Logistics and Accounting",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}