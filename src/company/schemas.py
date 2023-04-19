from sqlalchemy import Column, ForeignKey, SmallInteger, String, Uuid, Enum
from sqlalchemy.orm import relationship
from src.database import Base
#from src.user.schemas import User
import enum
import uuid
class CompanyMode(enum.Enum):
    DRAFT = 'D'
    PUBLISHED = 'P'

class Company(Base):
    __tablename__ = "company"
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String,nullable=False, unique=True)
    description = Column(String,)
    mode = Column(Enum(CompanyMode), nullable=False, default=CompanyMode.DRAFT)
    users = relationship('User',back_populates="company")
    rating = Column(SmallInteger, nullable=True , default = 0)