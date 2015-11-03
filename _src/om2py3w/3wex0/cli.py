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
        help, addr = s.recvfrom(2048)
        print help
    else:
        pass

s.close()