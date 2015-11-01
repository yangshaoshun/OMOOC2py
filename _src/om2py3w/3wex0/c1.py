#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:   
    line = raw_input(">>> ") 
    if line == 'q' or line == 'quit' or line == '':
        print "保存文件并推出..."
        break
    elif line == 'h' or line == '?' or line == 'help':
        print '''
        输入 q/quit/Enter 推出
        输入 ?/h/hlep 查看帮助
        '''
    else:
        s.sendto(line,address)
        print "sending request"
        #recvdata, addr = s.recvfrom(2048)
        #print recvdata

s.close()