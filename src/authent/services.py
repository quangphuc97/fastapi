from passlib.context import CryptContext
from src.settings import INFO_GENERATE_TOKEN
from sqlalchemy.orm import Session
from starlette import status
from src.user.schemas import User
from src.database import get_db_context
from datetime import datetime, timedelta
from src.user.services import get_user_by_username
from typing_extensions import Annotated
from typing import Union
from fastapi import Depends
from jose import JWTError, jwt
from fastapi import HTTPException
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_username(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=INFO_GENERATE_TOKEN["ACCESS_TOKEN_EXPIRE_MINUTES"])
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, INFO_GENERATE_TOKEN["SECRET_KEY"], algorithm=INFO_GENERATE_TOKEN["ALGORITHM"])
    return encoded_jwt




