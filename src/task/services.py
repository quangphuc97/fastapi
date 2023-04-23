from sqlalchemy.orm import Session
from .schemas import Task
from src.user.schemas import User
from uuid import UUID
def get_all_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def create_task(db: Session, db_task: Task):
    db.add(db_task)
    return db.commit()
def update_task_by_id(db: Session, task_update: Task, task_id:UUID):
    task_in_db = db.query(Task).filter(Task.id == task_id).first()
    if task_in_db is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task_in_db.user_id is not None and task_in_db.user_id != task_update.user_id:
        changed_user = db.query(User).filter(User.id == task_update.user_id).first()
        if changed_user is None:
            raise HTTPException(status_code=422, detail="Invalid user id")
    task_in_db.summary = task_update.summary
    task_in_db.description = task_update.description
    task_in_db.status = task_update.status
    task_in_db.priority = task_update.priority
    task_in_db.user_id = task_update.user_id
    db.add(task_in_db)
    db.commit()
    db.refresh(task_in_db)
    return task_in_db
def delete_task_by_id(db: Session, task_id:UUID):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return True
