#!/usr/bin/python
# -*- coding:utf-8 -*-
"""Event对象+Queue队列 = 实现线程间通信"""

import threading
from Queue import Queue


def creater(data, q):
    print(threading.currentThread().getName())
    print("creating data and put it on the queue")
    for item in data:
        evt = threading.Event()  # 创建 事件对象, --可以理解为指示状态的一个变量,比如挂起,等待,完成等
        q.put((item, evt))
        print("put data: {} int queue, and waiting for consumer".format(item))
        evt.wait()  # 设置等待,挂起自身线程, 等待evt.set()执行


def consumer(q):
    print(threading.currentThread().getName())
    while True:
        data, evt = q.get()  # Queue对象自动处理lock问题
        print("get data: {} from queue".format(data))
        res = data * 2
        print res
        evt.set()
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    data = [1, 2, 3, 4, 5]
    t1 = threading.Thread(target=creater, args=(data, q))
    t2 = threading.Thread(target=consumer, args=(q,))

    t1.start()
    t2.start()

    q.join() # Queue的join方法, 会告诉Queue等待所有线程结束