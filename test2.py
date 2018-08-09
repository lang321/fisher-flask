# coding:utf-8
from flask import Flask, current_app,request

app = Flask(__name__)
# 获取上下文
# ctx = app.app_context()
# ctx.push()
# a = current_app
# b= current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    b = current_app.config['DEBUG']

class MyResource(object):
    name = 'name'
    def __enter__(self):
        print('连接资源..')
        return self
    # exc_type
    # exc_val
    # exc_tb
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('exception..')
        else:
            print('no exception..')
        print('释放资源..')
        # with中发生了异常：如果返回false，with语句的外部会跑出异常
        return True

    def query(self):
        print('查询..')

with MyResource() as a:
    1/0
    a.query()