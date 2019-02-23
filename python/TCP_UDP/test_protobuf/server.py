# !/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import threading
import time
import google.protobuf
import require_pb2


def tcp_cb(sock, addr):
    assert isinstance(sock, socket.socket)
    assert isinstance(addr, tuple)

    print("Accept connection from %s:%s" % addr)
    # sock.send("Welcome from server".encode('utf-8'))
    buffer = []
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        buffer.append(data)
    datas = b''.join(buffer)
    res = require_pb2.AddressBook()
    res.ParseFromString(datas)

    for person in res.people:
        print("p_id{},p_name{},p_email{},p_money{},p_workstatu{}"
              .format(person.id, person.name, person.email, person.money, person.work_status))

        for phone_number in person.phones:
            print(phone_number.number, phone_number.type)

        for key in person.maps.mapfield:
            print(key, person.maps.mapfield[key])

    sock.close()
    print("Connection closed")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)  # 参数指定等待连接的最大数量, 超过的将被丢弃

print("Waiting for connection...")

while True:
    # 接受一个新连接
    sock, addr = s.accept()
    """
    sock: socket
    addr: 二元tuple,包含发送方的 (ip地址,端口)
    """
    # 创建新线程来处理这个TCP连接
    t = threading.Thread(target=tcp_cb, args=(sock, addr))
    t.start()

