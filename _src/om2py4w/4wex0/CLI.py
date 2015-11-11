#encoding=utf8
from bottle import *
import requests

read = requests.get('http://localhost:8080/log')
print read.text

#向表单提交信息
while True:
    line = raw_input(">>> ")
    if line == 'q' or line == 'quit' or line == '':
        break
    elif line == 'h' or line == '?' or line == 'help':
        print '''
        输入 q/quit/Enter 推出
        输入 ?/h/hlep 查看帮助
        '''
    elif line == 's':
        read = requests.get('http://localhost:8080/log')
        print read.text
    else:
        form_data = {'indata':line}
        r = requests.post('http://localhost:8080/text',data = form_data)
        continue