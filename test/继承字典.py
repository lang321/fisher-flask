# coding:utf-8
'''
@author: fight139
@file: 继承字典.py
@time: 2018/7/23 12:37
@desc: 
'''
class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super(MyDict, self).__init__(*args, **kwargs)
        self['modify'] = True

d = MyDict()
print(d)
