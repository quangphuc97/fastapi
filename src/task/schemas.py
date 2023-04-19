
import enum
import uuid
from src.database import Base
from sqlalchemy import Column, String, Uuid, ForeignKey, SmallInteger, Enum
from sqlalchemy.orm import relationship
class TaskStatus(enum.Enum):
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    REVIEW = 'Review'
    DONE = 'Done'

class Task():
    __tablename__ = "task"
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    summary = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.TODO)
    priority = Column(SmallInteger, nullable=True)
    user_id = Column(Uuid, ForeignKey("user.id"), nullable=True)


