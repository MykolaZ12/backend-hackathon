from sqlalchemy import Integer, Column, DateTime, func, String, Table, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from db.db import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    price = Column(Numeric(10, 2))
    status = Column(String(50))
    address = Column(String)
    items = Column(JSONB)
    volunteer = Column(Integer)
    date_created = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="user")
