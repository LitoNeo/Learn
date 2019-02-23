# !/usr/bin/python3
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
"""
socket.AF_INET 表示ipv4
socket.SOCK_STREAM 表示TCP
socket.SOCK_DGRAM 表示UDP
"""
s.bind(('127.0.0.1',9999))
"""注: UDP不需要添加listen监听, 因为UDP接收任何客户端的数据"""

print("Bind UDP on 9999...")
while True:
    data, addr = s.recvfrom(1024)   # udp在使用时要加上from/to, 可用以识别当前客户端
    # recvfrom 直接获取数据, 而不是socket连接(udp没有socket连接)
    print("Received from %s:%s" % addr)
    s.sendto(b'Hello, %s!' % data, addr)  # 此处sendto需要添加客户端地址
s.close()


