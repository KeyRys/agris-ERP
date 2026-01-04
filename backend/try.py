from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
DATABASE_URL = os.getenv("DATABASE_URL")

print(DATABASE_URL)