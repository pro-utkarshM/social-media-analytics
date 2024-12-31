from dotenv import load_dotenv
import os

load_dotenv()

ASTRA_CLIENT_ID = os.getenv("ASTRA_CLIENT_ID")
ASTRA_CLIENT_SECRET = os.getenv("ASTRA_CLIENT_SECRET")
ASTRA_DB_ENDPOINT = os.getenv("ASTRA_DB_ENDPOINT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

