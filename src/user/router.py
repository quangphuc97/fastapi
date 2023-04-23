from fastapi import APIRouter, Depends, Query
from src.common import api
from src.database import get_db_context
from .models import UserCreateModel, UserUpdateModel, UserModel
from sqlalchemy.orm import Session
from .schemas import User
from typing import List
from starlette import status
from .services import create_user, get_all_users, get_user_by_id, update_user_by_id, delete_user_by_id
from src.authent.services import get_password_hash
from src.authent.middwares import is_current_user_admin
from uuid import UUID
from datetime import datetime

router = APIRouter(prefix="/user", tags=["User"],
                   dependencies=[Depends(is_current_user_admin)])


@router.get("")
async def get_all(page: int = Query(ge=1, default=1),
                  size: int = Query(ge=1, le=50, default=10),
                  db: Session = Depends(get_db_context),
                  ) -> List[UserModel]:
    return get_all_users(db=db, skip=(page - 1) * size, limit=size)


@router.get("/{user_id}")
async def get_by_id(user_id: UUID,
                    db: Session = Depends(get_db_context),
                    ) -> UserModel:
    return get_user_by_id(db=db, id=user_id)


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update(request: UserUpdateModel,
                 user_id: UUID,
                 db: Session = Depends(get_db_context),
                 ):
    hashed_password = get_password_hash(request.password)
    user_update = User(**request.dict(exclude={"password"}), hashed_password=hashed_password,
                       updated_at=datetime.now())
    return update_user_by_id(db=db, id=user_id, user_update=user_update)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete(
        user_id: UUID,
        db: Session = Depends(get_db_context),
):
    return delete_user_by_id(db=db, id=user_id)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: UserCreateModel, db: Session = Depends(get_db_context)) -> None:
    dataCreate = request.dict()
    dataCreate["hashed_password"] = get_password_hash(dataCreate["password"])
    dataCreate.pop("password")
    user = User(**dataCreate)
    is_succeed = create_user(db, user) is not None
    if not is_succeed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server error")
    return None
