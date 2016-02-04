#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto('',address)
print "sending request"
history, addr = s.recvfrom(2048)
print history

while True:    
    line = raw_input(">>> ")
    s.sendto(line,address)
    if line == 's':       
        history, addr = s.recvfrom(2048)
        print history
    elif line == 'q':
        break
    elif line == '?' or line == 'h':
        print '''
        输入 s 同步日志记录
        输入 q/quit/Enter 推出
        输入 ?/h/hlep 查看帮助
        '''
    else:
        s.sendto(line,address)

s.close()