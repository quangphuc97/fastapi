from fastapi import APIRouter, Depends, Query, HTTPException
from .services import get_all_tasks, create_task , update_task_by_id, delete_task_by_id
from .models import TaskModel
from .schemas import Task
from src.database import get_db_context
from sqlalchemy.orm import Session
from starlette import status
from src.authent.middwares import is_current_user_admin
from uuid import UUID

router = APIRouter(prefix="/task", tags=["Task"], dependencies=[Depends(is_current_user_admin)])


@router.get("")
async def get_all(page: int = Query(ge=1, default=1),
                  size: int = Query(ge=1, le=50, default=10),
                  db: Session = Depends(get_db_context)):
    return get_all_tasks(db=db, skip=(page - 1) * size, limit=size)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: TaskModel, db: Session = Depends(get_db_context)) -> None:
    task = Task(**request.dict())
    return create_task(db, task)


@router.put("/{task_id}", status_code=status.HTTP_200_OK)
async def update(request: TaskModel, task_id: UUID, db: Session = Depends(get_db_context)) -> None:
    task_update = Task(**request.dict())
    return update_task_by_id(db=db,task_id=task_id, task_update=task_update)

@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
async def delete(task_id: UUID, db: Session = Depends(get_db_context)) -> None:
    return delete_task_by_id(db=db,task_id=task_id)