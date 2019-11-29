"""
Author: Zoulingbin
"""
from sqlalchemy import (Column, String, Integer, Float, ForeignKey)
from jian.interface import InfoCrud as Base, BaseCrud
from sqlalchemy.orm import relationship


class KuaiShou(BaseCrud):
    __tablename__ = 'kuaishou'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))
    kuaishou_num = Column(String(100), nullable=False, unique=True, comment='快手账号')
