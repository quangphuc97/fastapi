from fastapi import APIRouter, Depends, Query, HTTPException
from .services import get_all_companys, create_company
from .models import CompanyModel
from .schemas import Company
from src.database import get_db_context
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("")
async def get_all(page: int = Query(ge=1, default=1),
                  size: int = Query(ge=1, le=50, default=10),
                  db: Session = Depends(get_db_context)):
    return get_all_companys(db=db, skip=(page - 1) * size, limit=size)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: CompanyModel, db: Session = Depends(get_db_context)) -> None:
    company = Company(**request.dict())
    is_succeed = create_company(db, company) is not None
    if not is_succeed:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server error")
    return None
