# coding:utf-8
'''
@author: fight139
@file: auth.py
@time: 2018/7/21 10:37
@desc: 
'''
from datetime import timedelta

from flask import request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user

from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User
from app.models.base import db
from . import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        # db.session.commit()
        return redirect(url_for('web.login'))
    print(form.errors)
    return render_template('auth/register.html', form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            # 使用登录管理器 管理登录
            login_user(user, remember=True, duration=timedelta(seconds=20))
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或者密码错误')
    return render_template('auth/login.html', form=form)