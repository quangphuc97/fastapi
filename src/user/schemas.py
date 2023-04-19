import uuid
from src.database import Base
from sqlalchemy import Column, String, Uuid, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship
#from src.company.schemas import Company
class User(Base):
    __tablename__ = "user"
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=True)
    created_at = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True)
    company_id = Column(Uuid, ForeignKey("company.id"), nullable=True)
    company = relationship("Company")
