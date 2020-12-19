from datetime import datetime

from pydantic import BaseModel


# Order
from app.user.schemas import UserInResponse


class OrderBase(BaseModel):
    address: str
    price: bool
    items: str

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
