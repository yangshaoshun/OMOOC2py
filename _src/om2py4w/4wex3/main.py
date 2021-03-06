# -*- coding: utf-8 -*-
from bottle import * 
import sys
from jinja2 import Template

reload(sys)
sys.setdefaultencoding( "utf-8" )


def print_log():
    open_file = open("mydaily.log")
    log = open_file.read()
    return log

def new(txt_add):
    target = open("mydaily.log", 'a')
    target.write(txt_add + '\n')
    target.close()

@route('/')
@route('/text') #text 页面
def input(): #把text页面与 input 函数绑定，每次打开text 页面，得到 input 函数的返回值
    log = print_log()
    return template('in.tpl', history = log)

@route('/text', method ='POST')
def do_input():
    data = request.forms.get('indata')
    new(data)
    log = print_log()
    return template('in.tpl', history = log)

@route('/log')
def history():
    log = print_log()
    # 使用 jinja2 的模板
#    template = Template('{{history}}')
#    return template.render( history = log )
    # 使用 bottle 默认的模板
#    return template('{{history}}', history = log)
    return template('boot.tpl', history = log)

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)