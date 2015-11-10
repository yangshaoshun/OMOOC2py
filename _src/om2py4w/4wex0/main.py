# -*- coding: utf-8 -*-
from bottle import * 

@route('/')
@route('/text') #text 页面

def input(): #把text页面与 input 函数绑定，每次打开text 页面，得到 input 函数的返回值
    open_file = open("mydaily.log")
    history = open_file.read()
    return template('input1.tpl', history = history)

@route('/text', method ='POST')
def do_input():
    data = request.forms.get('indata')
    target = open("mydaily.log", 'a')
    target.write(data + '\n')
    target.close()
    open_file = open("mydaily.log")
    history = open_file.read()
    return template('input1.tpl', history = history)  

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)