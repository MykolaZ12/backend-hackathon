from datetime import datetime

from pydantic import BaseModel


# Order
class OrderBase(BaseModel):
    text: str

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderInDB(OrderBase):
    pass


class OrderInResponse(OrderBase):
    id: int
    date_created: datetime