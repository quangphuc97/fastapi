from fastapi import APIRouter, Depends, Query, HTTPException
from src.common import api
from src.database import get_db_context
from .models import UserModel
from sqlalchemy.orm import Session
from .schemas import User
from typing import List
from starlette import status
from .services import create_user, get_password_hash, get_all_users

router = APIRouter(prefix="/user", tags=["User"])

import json
@router.get("")
async def get_all(page: int = Query(ge=1, default=1),
                  size: int = Query(ge=1, le=50, default=10),
                  db: Session = Depends(get_db_context)):
    # users = db.query(User).all()
    # return users
    return get_all_users(db=db, skip=(page - 1) * size, limit=size)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: UserModel, db: Session = Depends(get_db_context)) -> None:
    dataCreate = request.dict()
    dataCreate["hashed_password"] = get_password_hash(dataCreate["password"])
    dataCreate.pop("password")
    user = User(**dataCreate)
    is_succeed = create_user(db, user) is not None
    if not is_succeed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server error")
    return None
