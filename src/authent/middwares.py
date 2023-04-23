from jose import JWTError, jwt
from fastapi import HTTPException
from starlette import status
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from src.settings import INFO_GENERATE_TOKEN

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def is_current_user_admin(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, INFO_GENERATE_TOKEN["SECRET_KEY"], algorithms=[INFO_GENERATE_TOKEN["ALGORITHM"]])
        username: str = payload.get("username")
        is_admin: bool = payload.get("is_admin")
        is_active: bool = payload.get("is_active")
        if username is None or is_admin is None or is_active is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    if not is_admin or not is_active:
        raise HTTPException(status_code=405, detail="No permission")
