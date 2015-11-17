# -*- coding: utf-8 -*-
from bottle import *
import requests
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

def print_log():
    read = requests.get('http://localhost:8080/log')
    print read.text

#向表单提交信息
def main():
    #运行先打印日志
    print_log()
    while True:
        line = raw_input(">>> ")
        if line in ['q','quit']:
            break
        elif line in ['h','help','?']:
            print '''
            输入 q/quit/Enter 推出
            输入 ?/h/hlep 查看帮助
            '''
        elif line == 's':
            print_log()
        else:
            form_data = {'indata':line}
            r = requests.post('http://localhost:8080/text',data = form_data)
            continue

if __name__ == __main__:
    main()