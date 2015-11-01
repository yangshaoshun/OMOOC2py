#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
while True:
        line = raw_input(">>> ")
        s.send(line)
        #if line == 'q' or line == 'quit' or line == '':
        #    target.close()
        #    print "保存文件并推出..."
        #    break
        #elif line == 'h' or line == '?' or line == 'help':
        #    print '''
        #    输入 q/quit/Enter 推出
        #    输入 ?/h/hlep 查看帮助
        #    '''
        #else:
        #    wtime = time.strftime('%Y-%m-%d %H:%M:%S')
        #    target.write(wtime + ' ' + line + '\n')

s.close                     # Close the socket when done