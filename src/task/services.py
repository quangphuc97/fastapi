from sqlalchemy.orm import Session
from .schemas import Task

def get_all_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def create_task(db: Session, db_task: Task):
    try:
        db.add(db_task)
        db.commit()
        return True
    except:
        return None
