# coding:utf-8
'''
@author: fight139
@file: user.py
@time: 2018/7/20 21:47
@desc: 
'''
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.models.base import Base


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    # 设置field默认名称, 密文
    _password = Column('password', String(128), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receiver_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd=None):
        '''
        设置密码
        :param pwd: 明文
        :return:
        '''
        if pwd:
            self._password = generate_password_hash(pwd)

    def check_password(self, pwd):
        '''
        检查密码是否和当前对象的密码一致
        :param pwd: 明文
        :return:
        '''
        return check_password_hash(self._password, pwd)

    def get_id(self):
        '''
        login_user保存的ID - 方法名固定
        :return: id
        '''
        return self.id

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))