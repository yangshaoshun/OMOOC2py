#!/usr/bin/python           # This is server.py file
# -*- coding: utf-8 -*-

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.send('这是一个日志软件，你可以输入单行文本')
    line = c.recv(1024)
    print line
    target = open("mydaily.log", 'a')
    target.write(line + '\n')

c.close()                # Close the connection