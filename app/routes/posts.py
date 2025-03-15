from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import PostCreate
from app.database import get_db
from app.caching import cache_get, cache_set
from app.dependencies import get_current_user_db
from app.crud import create_post, get_user_posts, delete_post

router = APIRouter()

@router.post("/addpost")
def add_post(post: PostCreate, user=Depends(get_current_user_db), db: Session = Depends(get_db)):
    new_post = create_post(db, user.id, post.text)
    return {"postID": new_post.id}

@router.get("/getposts")
def get_posts(user=Depends(get_current_user_db), db: Session = Depends(get_db)):
    cache_key = f"posts_{user.id}"
    cached_posts = cache_get(cache_key)
    if cached_posts:
        return cached_posts
    posts = get_user_posts(db, user.id)
    cache_set(cache_key, posts)
    return posts

@router.delete("/deletepost")
def delete_post(postID: int, user=Depends(get_current_user_db), db: Session = Depends(get_db)):
    deleted = delete_post(db, postID, user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}
