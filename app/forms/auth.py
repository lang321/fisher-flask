# coding:utf-8
'''
@author: fight139
@file: auth.py
@time: 2018/7/20 22:31
@desc: 
'''
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱格式不合法')])
    password = StringField(validators=[DataRequired(message='密码不能为空'), Length(6,32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称长度2-10')])

    # 这个函数由WTForm自动调用，field为email属性
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已经被注册')
class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱格式不合法')])
    password = StringField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])