from sqlalchemy.orm import Session
from .schemas import Company
from uuid import UUID
from fastapi import HTTPException
def get_all_companys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()


def create_company(db: Session, db_company: Company):
    db.add(db_company)
    db.commit()
    return True


def update_company_by_id(db: Session, company_update: Company, company_id:UUID):
    company_in_db = db.query(Company).filter(Company.id == company_id).first()
    if company_in_db is None:
        raise HTTPException(status_code=404, detail="Company not found")
    company_in_db.name = company_update.name
    company_in_db.description = company_update.description
    company_in_db.mode = company_update.mode
    company_in_db.rating = company_update.rating
    db.add(company_in_db)
    db.commit()
    db.refresh(company_in_db)
    return company_in_db


def delete_company_by_id(db: Session, company_id: UUID):
    company = db.query(Company).filter(Company.id == company_id).first()
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(company)
    db.commit()
    return True
