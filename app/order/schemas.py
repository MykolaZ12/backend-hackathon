from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.user.schemas import UserInResponse


# Order
class OrderBase(BaseModel):
    address: str
    price: bool
    items: Optional[str]
    full_name: str
    phone_number: str

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderInDB(OrderBase):
    user_id: int


class OrderInResponse(OrderBase):
    id: int
    date_created: datetime
    user: UserInResponse
