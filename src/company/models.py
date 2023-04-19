from pydantic import BaseModel, Field
from .schemas import CompanyMode
from typing import Optional, Union

class CompanyModel(BaseModel):
    name: str
    description: Optional[str]
    mode: CompanyMode = Field(default=CompanyMode.DRAFT)
    rating: Union[int, None] = Field(
        default=0, title="ratting of company", ge=0, le=5
    )
