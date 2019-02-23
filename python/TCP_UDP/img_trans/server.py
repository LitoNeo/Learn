#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import cv2
import numpy as np
import socket


class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', 9999))
        self.sock.listen(True)
        print("Server is ready...")

    def recv_size(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def recv_all(self, sock, count):
        buf = b''
        while count:
            # For python
            newbuf = sock.recv(1)
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def run(self):
        sock, addr = self.sock.accept()
        while True:
            length = self.recv_size(sock, 16)
            if length is not None:
                stringData = self.recv_all(sock, int(length))
                data = np.fromstring(stringData, dtype='uint8')
                decimg = cv2.imdecode(data, 1)
                cv2.imshow('Server', decimg)
                if cv2.waitKey(25) == ord('q'):
                    break
                print("received length: {}".format(length))
                sock.send("Server has received your image.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        cv2.destroyAllWindows()
        return self


if __name__ == '__main__':
    with Server() as server:
        server.run()
