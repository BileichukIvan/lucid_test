from sqlalchemy.orm import Session
from app.models import User, Post


def create_user(db: Session, email: str, password: str):
    new_user = User(email=email, password=password)
    db.add(new_user)
    db.commit()
    return new_user


def authenticate_user(db: Session, email: str, password: str):
    return db.query(User).filter(User.email == email, User.password == password).first()


def create_post(db: Session, user_id: int, text: str):
    new_post = Post(user_id=user_id, text=text)
    db.add(new_post)
    db.commit()
    return new_post


def get_user_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()


def delete_post(db: Session, post_id: int, user_id: int):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post
