#!/usr/bin/python
# -*- coding:utf-8

import socket
import threading


# class Listener:
#     def __init__(self, ip, port):
#         self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.listener.bind((ip, port))
#         print("listener_thread name: {}".format(threading.currentThread().getName()))
#
#     def run(self):
#         while True:
#             data, addr = self.listener.recvfrom(1024)
#             print("The other: ")
#             print(data)
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.listener.close()
#
#
# class Talker:
#     def __init__(self, ip, port):
#         self.talker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.target = (ip, port)
#         print("talker_thread name: {}".format(threading.currentThread().getName()))
#
#     def run(self):
#         a = raw_input("Me: ")
#         self.talker.sendto(a, self.target)
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.talker.close()
#
#
# class App:
#     def __init__(self):
#         self.name = "wechat_fake"
#
#     def run(self):
#         print("start wechat...")
#         listener = Listener('127.0.0.1', 8888)
#         talker = Talker('127.0.0.1', 9999)
#
#         t_listener = threading.Thread(target=listener.run, name="listener")
#         t_listener.start()
#         t_talker = threading.Thread(target=talker.run, name="talker")
#         t_talker.start()
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return self
#
#
# if __name__ == '__main__':
#     with App() as app:
#         app.run()


class Listener(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.listener.bind((ip, port))

    def run(self):
        print("listener_thread name: {} \n".format(threading.currentThread().getName()))
        while True:
            data, addr = self.listener.recvfrom(1024)
            if data == 'exit':
                print("The other close the connection, enter 'exit' to exit.")
                break
            print(">>: " + data)
        self.listener.close()

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.listener.close()


class Talker(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.talker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.target = (ip, port)
        print("talker_thread name: {}".format(threading.currentThread().getName()))

    def run(self):
        while True:
            a = raw_input()
            # print("Me: " + a)
            self.talker.sendto(a, self.target)
            if a == 'exit':
                break
        self.talker.close()

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.talker.close()


class App:
    def __init__(self):
        self.name = "wechat_fake"

    def run(self):
        print("start wechat...")
        listener = Listener('127.0.0.1', 9999)
        listener.setName("listener")
        listener.start()

        talker = Talker('127.0.0.1', 8888)
        talker.setName("talker")
        talker.start()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self


if __name__ == '__main__':
    with App() as app:
        app.run()