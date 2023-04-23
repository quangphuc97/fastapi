from sqlalchemy.orm import Session
from .schemas import User
from src.common.enum import OrderType
from passlib.context import CryptContext
from datetime import datetime
from uuid import UUID
from .models import UserUpdateModel, UserModel
from src.company.schemas import Company
from fastapi import HTTPException


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, db_user: User):
    db_user.created_at = datetime.utcnow()
    db.add(db_user)
    db.commit()
    return True


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()



def get_user_by_id(db: Session, id: UUID):
    return db.query(User).filter(User.id == id).first()



def update_user_by_id(db: Session, id: UUID, user_update:User):
    user_in_db = db.query(User).filter(User.id == id).first()
    if user_in_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user_update.company_id is not None and user_in_db.company_id != user_update.company_id:
        changed_company = db.query(Company).filter(Company.id == user_update.company_id).first()
        if changed_company is None:
            raise HTTPException(status_code=422, detail="Invalid company information")
    user_in_db.email = user_update.email
    user_in_db.username = user_update.username
    user_in_db.hashed_password = user_update.username
    user_in_db.first_name = user_update.first_name
    user_in_db.last_name = user_update.last_name
    user_in_db.is_active = user_update.is_active
    user_in_db.is_admin = user_update.is_admin
    user_in_db.updated_at = user_update.updated_at
    user_in_db.company_id = user_update.company_id
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db


def delete_user_by_id(db:Session,id: UUID):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return True
