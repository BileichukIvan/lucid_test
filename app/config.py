import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
CACHE_EXPIRY = int(os.getenv("CACHE_EXPIRY", 300))  # 5 хвилин
