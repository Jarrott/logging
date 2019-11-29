# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/21 <https://www.soo9s.com>
"""
from jian import db
from sqlalchemy import (Column, String, Integer, Float)
from jian.interface import BaseCrud as Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(50), nullable=False, unique=True)
    nickname = Column(String(24), nullable=False, unique=True)
    _password = Column('password', String(128), nullable=False)
    invite_code = Column(String(20), default=0, comment='邀请码')
    commission = Column(Float, default=0, comment='佣金')
