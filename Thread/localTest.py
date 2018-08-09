# coding:utf-8
import threading
import time

from werkzeug.local import Local, LocalStack


class A(object):
    a = 100

obj = Local()
obj.a = 1

s = LocalStack()
s.push(100)


def fun():
    obj.a = 20
    print('in new thread obj.a ia', obj.a)
    print(s.top)
    s.push('new word')
    print(s.top)


if __name__ == '__main__':
    t = threading.Thread(target=fun, name='mythread')
    t.start()
    time.sleep(1)
    print('in main thread obj.a is' ,obj.a)
    print(s.top)

    d = {'name':'jon'}
    print(d.get('name'))
