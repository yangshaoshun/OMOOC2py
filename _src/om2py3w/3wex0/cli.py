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
    msg = raw_input(">>> ")
    s.sendto(msg,address) 
    line, addr = s.recvfrom(2048)
    if line == 'q':
        break
    print line
    
s.close()