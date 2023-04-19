from sqlalchemy.orm import Session
from .schemas import Company

def get_all_companys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()


def create_company(db: Session, db_company: Company):
    try:
        db.add(db_company)
        db.commit()
        return True
    except:
        return None
