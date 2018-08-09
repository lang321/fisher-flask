# coding:utf-8
'''
@author: fight139
@file: gift.py
@time: 2018/7/20 21:55
@desc: 
'''
from sqlalchemy import Column, Integer, Boolean, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship, backref

from app.models.base import db, Base


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    uid = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User',backref = backref('gifts',order_by=id))

    bid = Column(Integer, ForeignKey('book.id', ondelete='CASCADE'))
    book = relationship('Book')
    lauched = Column(Boolean, default=False)
