from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base properties"""
    role: str
    phone_number: str
    full_name: str
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDB(UserBase):
    id: int
    hashed_password: str


class UserInResponse(UserBase):
    id: int
    full_name: Optional[str] = None
    date_registrations: datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
