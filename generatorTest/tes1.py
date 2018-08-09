# coding:utf-8
'''
@author: fight139
@file: tes1.py
@time: 2018/7/22 10:08
@desc: 
'''

class A(object):
    def show(self):
        print('hello')

def fun():
    print('enter')
    yield A()
    print('exit')

def fib(max):
    n, a, b = 0, 0, 1
    while max > n:
        yield b
        a, b = b, a + b
        n = n + 1
    return print('done')

if __name__ == '__main__':
    f = fib(5)
    print(f)
    # print(f.__next__())
    # print(',')
    # print(f.__next__())
    # print(',')
    # print(f.__next__())

    print('====')
    for i in f:
        print(i)


    a = fun()
    print(a)
    a.__next__().show()
    a.__next__()
