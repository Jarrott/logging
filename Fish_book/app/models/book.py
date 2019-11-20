from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Book(Base):

    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未知', nullable=False)
    binding = Column(String(20))
    publisher = Column(String(50), comment='出版社')
    price = Column(String(20), comment='价格')
    Pages = Column(Integer, comment='页数')
    pubdate = Column(String(20), comment='出版日期')
    isbn = Column(String(15), nullable=False, unique=True, comment='isbn编码')
    summary = Column(String(1000), comment='简介')
    image = Column(String(50))
