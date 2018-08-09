# coding:utf-8

# 蓝图  name, 所在的模块
from flask import Blueprint

web = Blueprint('web', __name__)
# print('web1', id(web))

from app.web import book
from app.web import user
from app.web import auth
from app.web import gift


# 同一个模块，只会导入一次，