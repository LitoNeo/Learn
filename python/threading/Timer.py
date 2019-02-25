#!/usr/bin/python
# -*- coding:utf-8 -*-
""" 定时器Timer:
用以实现指定时间后要发生的动作
"""
import subprocess  # fork一个子进程, 并运行一个外部的程序
from threading import Timer

kill = lambda process: process.kill()
cmd = ['ping', 'www.baidu.com']
ping = subprocess.Popen(cmd, subprocess.STDOUT, stderr=subprocess.PIPE) # Popen生成子进程
my_timer = Timer(5, kill, [ping])  # 5s后 kill(函数)掉 [ping]   --ping.kill() 终止子进程
# subprocess.PIPE 缓冲区, 等待communicate取走
# subprocess.STDOUT 标准输出

try:
    my_timer.start()
    stdout, stderr = ping.communicate() # communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成, 并取走缓冲区数据
finally:
    my_timer.cancel()

print(str(stdout))

"""subprocess
child.poll() # 检查子进程状态
child.kill() # 终止子进程
child.send_signal() # 向子进程发送信号
child.terminate() # 终止子进程
"""

