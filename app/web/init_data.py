# coding:utf-8
'''
@author: fight139
@file: init_data.py
@time: 2018/7/29 14:32
@desc: 
'''

from app import db
from app.models.book import Book
from app.models.user import User
from . import web



# 测试数据
@web.route('/user/init')
def init_user():
    # user
    users = [User(nickname='admin', phone_number='18666666666', email='1392242530@qq.com')]
    users[0].password = '123456'
    with db.auto_commit():
        db.session.add(users)

@web.route('/book/init')
def init_book():
    books = [Book(title='java', author='李刚', price=20, isbn='35986547845', summery='概况'),
             Book(title='python', author='join', price=20, isbn='35983547845', summery='概况'),]
    with db.auto_commit():
        db.session.add_all(books)


