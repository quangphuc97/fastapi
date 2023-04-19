from sqlalchemy.orm import Session
from .schemas import User
from src.common.enum import OrderType
from passlib.context import CryptContext
from datetime import datetime


def verify_password(plain_password, hashed_password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, db_user: User):
    try:
        db_user.created_at = datetime.utcnow()
        db.add(db_user)
        db.commit()
        return True
    except:
        return None
