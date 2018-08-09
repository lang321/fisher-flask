# coding:utf-8
import re


class A(object):
    pass


if __name__ == '__main__':
    # a = A()
    # a.num = 10
    # print(a.num)
    # b = object()
    # b.num = 20
    # print(b.num)

    s = '12344546111'
    r = re.match('^\d{11}$', s)
    print(r.group())