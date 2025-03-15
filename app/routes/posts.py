from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import PostCreate
from app.database import get_db
from app.auth import get_current_user
from app.crud import create_post, get_user_posts, delete_post

router = APIRouter()

@router.post("/addpost")
def add_post(post: PostCreate, token: str, db: Session = Depends(get_db)):
    user_email = get_current_user(token)
    user = db.query(User).filter(User.email == user_email).first()
    new_post = create_post(db, user.id, post.text)
    return {"postID": new_post.id}

@router.get("/getposts")
def get_posts(token: str, db: Session = Depends(get_db)):
    user_email = get_current_user(token)
    user = db.query(User).filter(User.email == user_email).first()
    return get_user_posts(db, user.id)

@router.delete("/deletepost")
def delete_post(postID: int, token: str, db: Session = Depends(get_db)):
    user_email = get_current_user(token)
    user = db.query(User).filter(User.email == user_email).first()
    deleted = delete_post(db, postID, user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}
