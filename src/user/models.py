from pydantic import BaseModel,Field, EmailStr
from datetime import datetime
from uuid import UUID
from typing import Union

password_regex = "(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*?[#?!@$%^&*-]).{8,32}"

class UserModel(BaseModel):
    email: EmailStr
    first_name: Union[str, None] = Field(
        default=None, title="the first name of account", max_length=30, min_length=2
    )
    last_name: Union[str, None] = Field(
        default=None, title="the last name of account", max_length=30, min_length=2
    )
    is_active: bool
    is_admin: bool
    username: Union[str, None] = Field(
        default=None, title="the username of account", max_length=30, min_length=3
    )
    password: Union[str, None] = Field(
        default=None, title="the password of account",  regex=password_regex
    )

    company_id: Union[str, None] = Field(
        default=None, title="company id user",
    )