from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .models import Token
from .services import authenticate_user, create_access_token
from src.settings import INFO_GENERATE_TOKEN
from sqlalchemy.orm import Session
from src.database import get_db_context
from starlette import status
from typing_extensions import Annotated
from datetime import timedelta
from fastapi import HTTPException
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db_context)
) -> Token:
    user = authenticate_user(username=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=INFO_GENERATE_TOKEN["ACCESS_TOKEN_EXPIRE_MINUTES"])
    access_token = create_access_token(
        data={"username": user.username, "is_admin": user.is_admin, "is_active": user.is_active},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
