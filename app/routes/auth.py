from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserLogin
from app.database import get_db
from app.auth import generate_token
from app.crud import create_user, authenticate_user

router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if authenticate_user(db, user.email, user.password):
        raise HTTPException(status_code=400, detail="Email already registered")
    create_user(db, user.email, user.password)
    return {"token": generate_token(user.email)}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": generate_token(user.email)}
