# coding:utf-8
from flask import Blueprint

from app import db
from app.models.user import User
from . import web

@web.route('/user/delete', methods=['GET', 'POST'])
def delete():
    user = User.query.filter_by(id=3).first()
    with db.auto_commit():
        db.session.query(User).filter(User.id==1).delete()

    return 'ok'


