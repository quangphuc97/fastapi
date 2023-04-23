from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from uuid import UUID
from typing import Union

password_regex = "(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*?[#?!@$%^&*-]).{8,32}"


class UserCreateModel(BaseModel):
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
        default=None, title="the password of account", regex=password_regex
    )

    company_id: Union[str, None] = Field(
        default=None, title="company id user",
    )


class UserModel(BaseModel):
    id: Union[UUID, None]
    email: Union[str, None]
    first_name: Union[str, None]
    last_name: Union[str, None]
    is_active: Union[bool, None]
    is_admin: Union[bool, None]
    username: Union[str, None]
    hashed_password: Union[str, None]
    company_id: Union[UUID, None]
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]

    class Config:
        orm_mode = True



class UserUpdateModel(BaseModel):
    email: Union[EmailStr, None] = Field(
        default=None
    )
    first_name: Union[str, None] = Field(
        default=None, max_length=30, min_length=2
    )
    last_name: Union[str, None] = Field(
        default=None, max_length=30, min_length=2
    )
    is_active: Union[bool, None] = Field(
        default=None
    )
    is_admin: Union[bool, None] = Field(
        default=None
    )
    username: Union[str, None] = Field(
        default=None, title="the username of account", max_length=30, min_length=3
    )
    password: Union[str, None] = Field(
        default=None, title="the password of account", regex=password_regex
    )

    company_id: Union[str, None] = Field(
        default=None, title="company id user",
    )
