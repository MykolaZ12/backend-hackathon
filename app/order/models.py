from sqlalchemy import Integer, Column, DateTime, func, String, Table
from sqlalchemy.dialects.postgresql import JSONB


from db.db import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    status = Column(String(50))
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    items = Column(JSONB)
