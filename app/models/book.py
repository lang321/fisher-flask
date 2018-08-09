
from sqlalchemy import Column, Integer, String, Float

from app.models.base import Base


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(20), nullable=False)
    price = Column(Float, nullable=True, default=0)
    isbn = Column(String(15), nullable=False, unique=True)
    summery = Column(String(200), default='没有简介')
