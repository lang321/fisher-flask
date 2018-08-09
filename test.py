# coding:utf-8
import os

from werkzeug.security import generate_password_hash

from app.models.user import User
from app.models.base import db



class A(object):
    def __init__(self):
        self.name = 'admin'
        self._age = 20
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    def fun(self):
        print("method A ....")


class B(A):
    def fun(self):
        print("method B")
        super().fun()


def swap(a, b):
    return b, a


if __name__ == '__main__':
    # num = 100
    # from app.test.a import num
    # print(num)
    dict = {'name':'join', 'age':20}
    print('name' in dict)
    print(None or 'hello')

    # arr = filter(lambda x: True if x else False, [None, 'hello', 'world', False])
    # print('/'.join(arr))

    print('-----')
    # user = User()
    # user.nickname = 'admin'
    # user.password = '123'
    # user.email = 'admin@qq.com'
    # user.phone_number = '13922425302'
    # db.session.add(user)
    # db.session.commit()
    print(os.path.basename('a/b/c'))