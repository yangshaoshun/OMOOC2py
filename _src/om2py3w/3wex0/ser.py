#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:
    data, addr = s.recvfrom(2048)
    if data == 's' or data == '':
        target = open("mydaily.log")
        s.sendto(target.read(), addr)
        target.close()
        continue #解决了无论如何都会执行 else 后面语句块的问题
    elif data == 'q':
        s.sendto('q', addr)
    	break
    elif data == '?':
        help = '''
        输入 s 同步日志记录
        输入 q/quit/Enter 推出
        输入 ?/h/hlep 查看帮助
        '''
        s.sendto(help, addr)
    else:
        print "received:", data, "from", addr   
        target = open("mydaily.log", 'a')
        target.write(data + '\n')
        target.close()
        s.sendto('',addr)

s.close()