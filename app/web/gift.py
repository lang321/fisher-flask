# coding:utf-8
'''
@author: fight139
@file: gift.py
@time: 2018/7/21 17:26
@desc: 
'''
from app import db
from app.models.gift import Gift
from app.web import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gift'


@web.route('/gifts/book/<bid>')
@login_required
def save_to_gift(bid):
    # 事务
    with db.auto_commit():
        gift = Gift()
        gift.bid = bid
        gift.uid = current_user.id
        current_user.beans = 1
        db.session.add(gift)
    return 'ok'
