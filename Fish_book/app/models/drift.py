from flask import current_app
from sqlalchemy.orm import relationship

from app.libs.enums import PendingStatus
from app.models.base import Base, db
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger, desc, func
from app.spider.yushu_book import YuShuBook


class Drift(Base):
    __tablename__ = 'dirft'

    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(20), nullable=False, comment='收件人姓名')
    address = Column(String(100), nullable=False, comment='收件地址')
    message = Column(String(200), comment='收件备注')
    mobile = Column(String(20), nullable=False, comment='收件人电话')
    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))
    # requester_id = Column(Integer, ForeignKey('user.id'))
    # requester = relationship('User')
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))
    _pending = Column('pending', SmallInteger, default=1)
    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift')

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value
