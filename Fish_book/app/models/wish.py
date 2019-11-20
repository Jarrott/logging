from sqlalchemy.orm import relationship
from app.models.base import Base, db
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger, desc, func
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # book_id = Column(Integer, ForeignKey('book_id'))
    isbn = Column(String(20), nullable=False)
    launched = Column(Boolean, default=False)
    status = Column(SmallInteger, default=1)

    @classmethod
    def get_my_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gift_count(cls, isbn_list):
        from app.models.gift import Gift

        count_list = db.session.query(
            func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(Gift.isbn).all()
        count_dict = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_dict

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


