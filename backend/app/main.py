import psycopg2
from dotenv import load_dotenv
import os
DATABASE_URL = os.getenv("DATABASE_URL")

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
    return {"message": "App is running"}

@app.get("/dbtest")
def db_test():
    """Attempt to connect to the database and print the result."""
    if not DATABASE_URL:
        print("Error: DATABASE_URL not found in environment variables.")
        return False    

    try:
        # Attempt to establish a connection
        conn = psycopg2.connect(DATABASE_URL)
        # If connection is successful
        print("Success: FastAPI is connected to the Supabase database!")
        conn.close()
        return True
    except OperationalError as e:
        # If connection fails
        print(f"Error: Database connection failed. Details: {e}")
        return False