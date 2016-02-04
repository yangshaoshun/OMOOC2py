#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:

    data, addr = s.recvfrom(2048)
    print data == 's'
    if data == 's' or data == '':
        target = open("mydaily.log")
        s.sendto(target.read(), addr)
    if data == 'q':
    	break
    else:
        print "received:", data, "from", addr        
        target = open("mydaily.log", 'a')
        target.write(data + '\n')
        target.close()

s.close()