# coding:utf-8
'''
@author: fight139
@file: test1.py
@time: 2018/7/23 12:03
@desc: 
'''

url_map = {}

def route(options):
    def inner(func, *args, **kwargs):
        url_map[options['path']] = func
        return func
    return inner

@route({'path':'/index'})
def index():
    print('index')

index()

class A(object):
    def __call__(self, *args, **kwargs):
        print('call')

a = A()
a()