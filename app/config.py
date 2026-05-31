import os
from dotenv import load_dotenv

load_dotenv()  # reads .env from project root

MYSQL_URL = os.getenv(
    "MYSQL_URL"
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not MYSQL_URL:
    raise RuntimeError("MYSQL_URL environment variable is not set")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY environment variable is not set")