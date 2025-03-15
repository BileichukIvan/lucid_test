from fastapi import HTTPException
import secrets
import time

tokens = {}

SECRET_KEY = "supersecret"  # Unsafe better use load.env()


def generate_token(email: str):
    token = secrets.token_hex(16)
    tokens[token] = {"email": email, "created": time.time()}
    return token


def get_current_user(token: str):
    if token not in tokens or time.time() - tokens[token]["created"] > 3600:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return tokens[token]["email"]
