#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
针对多个线程访问同一资源的情况,实现线程同步和线程锁
"""

import threading

total = 0
""" 单锁 """
# lock = threading.Lock()
#
# def update(x):
#     global total
#     with lock:    # 使用with 代替 try/finally操作
#         print threading.currentThread().getName()
#         total += x
#     print total
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         t = threading.Thread(target=update, args=(i,))
#         t.start()


""" 复锁 """
# 针对多个线程同时访问多个函数的情况, 用以将其隔离开

lock = threading.RLock()  # RLock()   --如果该处使用Lock(), 则由于lock的嵌套acquaire(), 会导致程序挂起
def function_1():
    print(threading.currentThread().getName())
    with lock:
        print("Function 1")
    print("End of Function 1")
    return("Done Function 1")

def function_2():
    print(threading.currentThread().getName())
    with lock:
        print("Function 2")
    print("End of Function 2")
    return("Done Function 2")

def main():
    with lock:
        res1 = function_1()
        res2 = function_2()
    print(res1)
    print(res2)


if __name__ == '__main__':
    # main()
    for i in range(2):
        t = threading.Thread(target=main)
        t.start()










