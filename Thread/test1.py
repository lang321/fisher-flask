# coding:utf-8
import threading

from werkzeug.local import LocalStack


def worker():
    print('new thread..')
    print(threading.current_thread().getName())

if __name__ == '__main__':
    # print('hello')
    # t = threading.current_thread()
    # print(t.getName())  # MainThread
    # th1 = threading.Thread(target=worker, name='my Thread')
    # th1.start()
    s = LocalStack()
    s.push(20)
    print(s.top)
    s.push(30)
    print(s.pop())
    print(s.top)

    print('123' or 'hello')