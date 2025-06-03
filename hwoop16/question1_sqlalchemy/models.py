from sqlalchemy import Column, Integer, String, Numeric
from db import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    price = Column(Numeric, nullable=False)
