from db import Base
from sqlalchemy import Column, Integer, String, DateTime
import datetime


class Test(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)


class Test2(Base):
    __tablename__ = "test_table_2"

    id = Column(Integer, primary_key=True)
    text = Column(String)

    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
