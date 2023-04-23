from fastapi import APIRouter, Depends, Query, HTTPException
from .services import get_all_companys, create_company, update_company_by_id , delete_company_by_id
from .models import CompanyModel
from .schemas import Company
from src.database import get_db_context
from sqlalchemy.orm import Session
from starlette import status
from src.authent.middwares import is_current_user_admin
from uuid import UUID

router = APIRouter(prefix="/company", tags=["Company"], dependencies=[Depends(is_current_user_admin)])


@router.get("")
async def get_all(page: int = Query(ge=1, default=1),
                  size: int = Query(ge=1, le=50, default=10),
                  db: Session = Depends(get_db_context)):
    return get_all_companys(db=db, skip=(page - 1) * size, limit=size)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: CompanyModel, db: Session = Depends(get_db_context)) -> None:
    company = Company(**request.dict())
    return create_company(db, company)


@router.put("/{company_id}", status_code=status.HTTP_200_OK)
async def update(company_id: UUID, request: CompanyModel, db: Session = Depends(get_db_context)) -> None:
    company_update = Company(**request.dict())
    return update_company_by_id(db=db, company_update=company_update, company_id=company_id)


@router.delete("/{company_id}", status_code=status.HTTP_200_OK)
async def delete(company_id: UUID, db: Session = Depends(get_db_context)) -> None:
    return delete_company_by_id(db=db, company_id=company_id)
