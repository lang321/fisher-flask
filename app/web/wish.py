# coding:utf-8
'''
@author: fight139
@file: wish.py
@time: 2018/7/24 16:37
@desc: 
'''
from app.web import web


@web.route('/my/wish')
def my_wish():
    return 'my wish'