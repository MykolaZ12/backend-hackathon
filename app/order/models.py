from sqlalchemy import Integer, Column, DateTime, func, String, Table, Numeric, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from db.db import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    price = Column(Boolean, default=False)
    status = Column(String(50), default="open")
    address = Column(String)
    items = Column(String)
    volunteer = Column(Integer)
    date_created = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="user")
