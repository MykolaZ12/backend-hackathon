from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from db.db import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    phone_number = Column(String(15))
    role = Column(String)
    hashed_password = Column(String)
    full_name = Column(String(255))
    date_registrations = Column(DateTime(), default=datetime.utcnow, index=True)
    last_login = Column(DateTime(), nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    avatar = Column(String, nullable=True)
