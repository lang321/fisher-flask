# coding:utf-8


# num2 = 2000
#
# print('test2',id(num))
from contextlib import contextmanager


class MyResouce(object):
    # def __enter__(self):
    #     print('enter..')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('exit..')

    def query(self):
        print('query...')

# with MyResouce() as r:
#     r.query()

# 在不改变MyResource的情况下，给这个类添加上下文管理器
@contextmanager
def my_resource():
    print('enter..')
    yield MyResouce()
    print('exit..')
    raise Exception('my exception')

with my_resource() as r:
    r.query()