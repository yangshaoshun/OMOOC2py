# -*- coding: utf-8 -*-
from bottle import * 
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

'''
def history():
    open_file = open("mydaily.log")
    history = open_file.read()
'''

def new(txt_add):
    target = open("mydaily.log", 'a')
    target.write(txt_add + '\n')
    target.close()

@route('/')
@route('/text') #text 页面

def input(): #把text页面与 input 函数绑定，每次打开text 页面，得到 input 函数的返回值
    open_file = open("mydaily.log")
    history = open_file.read()
    return template('input.tpl', history = history)

@route('/text', method ='POST')
def do_input():
    data = request.forms.get('indata')
    new(data)
    open_file = open("mydaily.log")
    history = open_file.read()
    return template('input.tpl', history = history)  

@route('/log')
def history():
    open_file = open("mydaily.log")
    history = open_file.read()
    return template('history.tpl', history = history)

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)