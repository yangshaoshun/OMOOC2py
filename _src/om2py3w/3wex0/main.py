#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
"""

Usage:
  main.py (s|c)
  main.py (-h|--help)
  main.py --version

Options:
  -h --help     Show this screen
  --version     Show version

"""

from docopt import docopt
import socket

def server():
    address = ('127.0.0.1', 31500)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)

    while True:
        data, addr = s.recvfrom(2048)
        if data == 's' or data == '':
            target = open("mydaily.log")
            s.sendto(target.read(), addr)
            target.close()
            continue
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

def client():
    address = ('127.0.0.1', 31500)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto('',address)
    #print "sending request"
    history, addr = s.recvfrom(2048)
    print history

    while True:    
        line = raw_input(">>> ")
        s.sendto(line,address) 
        msg, addr = s.recvfrom(2048)    
        if msg == 'q':
            break
        elif msg == '':
            continue
        else:
            print msg

    s.close()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Mydaily3.0')
    if arguments['s']:
        server()
    if arguments['c']:
        client()