from sqlalchemy import Integer, Column, DateTime, func, String, Table, Numeric
from sqlalchemy.dialects.postgresql import JSONB


from db.db import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    price = Column(Numeric(10, 2))
    status = Column(String(50))
    address = Column(String)
    items = Column(JSONB)
    date_created = Column(DateTime(timezone=True), server_default=func.now())

