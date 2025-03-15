from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import User


def get_current_user_db(token: str, db: Session = Depends(get_db)):
    """Dependency to get the current user based on token authentication"""
    user_email = get_current_user(token)
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
