# !/usr/bin/python3
# -*- coding: utf-8 -*-
import socket


# ## --- Test ---
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# buffer = []
# while True:
#     d = s.recv(1024)  # 最大每次接收1024字节
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# """
# b'' 是一个空字符
# buffer 是一个 字节列表
# b''.join(buffer) 表示使用空字节将buffer这个字节列表链接起来,组成一个新的<字节串>    注:要打印出来则需要解码成utf等格式
#     注: 此为python3的新特性, python2中的join只能链接字符串,not 字节串
# """
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('sina.html','wb') as f:
#     f.write(html)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

# print(s.recv(1024).decode('utf-8'))
for data in ['Hello', 'Internet', '!']:
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
s.send('exit'.encode('utf-8'))
s.close()
