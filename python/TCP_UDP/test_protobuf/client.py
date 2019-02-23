# !/usr/bin/python2.7
# -*- coding: utf-8 -*-
import google.protobuf
import require_pb2
import socket

class client(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr_server = ('127.0.0.1',9999)

    def run(self):
        print("run")
        address_book = require_pb2.AddressBook()
        person = address_book.people.add()

        person.id = 1
        person.name = "safly"
        person.email = "safly@qq.com"
        person.money = 1000.11
        person.work_status = True

        phone_number = person.phones.add()
        phone_number.number = "123456"
        phone_number.type = require_pb2.MOBILE

        maps = person.maps
        maps.mapfield[1] = 1
        maps.mapfield[2] = 2

        ser_res = address_book.SerializeToString()
        print("start connect server...")
        self.sock.connect(self.addr_server)
        self.sock.sendall(ser_res)

    def __enter__(self):
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.sock.close()
        return self




if __name__ == "__main__":
    with client() as app:
        app.run()

