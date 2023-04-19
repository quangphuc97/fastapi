from pydantic import BaseModel,Field, EmailStr
from datetime import datetime
from uuid import UUID
from typing import Union
from .schemas import TaskStatus
class TaskModel(BaseModel):
    summary: str
    description: str
    status: TaskStatus = Field(default=TaskStatus.TODO)
    priority: Union[int, None] = Field(
        default=0, title="the priority of account", ge=0, le=5
    )
    user_id: Union[str, None] = Field(
        default=None, title="user id",
    )