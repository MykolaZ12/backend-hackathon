from datetime import datetime

from pydantic import BaseModel


# Order
class OrderBase(BaseModel):
    address: str
    price: float = None
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