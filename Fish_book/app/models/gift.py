from flask import current_app
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger, desc, func
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # book_id = Column(Integer, ForeignKey('book_id'))
    isbn = Column(String(20), nullable=False)
    launched = Column(Boolean, default=False)
    status = Column(SmallInteger, default=1)

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def recent(cls):
        recent_gift = cls.query.filter_by(launched=False).group_by(Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        print(recent_gift)
        return recent_gift

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_my_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def wish_count(cls, isbn_list):
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                                                             Wish.isbn.in_(isbn_list),
                                                                             Wish.status == 1).group_by(Wish.isbn).all()
        count_dict = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_dict

    def delete(self):
        self.status = 0
