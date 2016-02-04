# -*- coding: utf-8 -*-
from bottle import * 

def print_log():
    open_file = open("mydaily.log")
    log = open_file.read()
    return log

@route('/text')
def input():
    return'''
        <form action="/text" method="post">
        <p>请输入单行日记: <input type="text" name="fname" /></p>
        <input type="submit" value="确认" />
        </form>

    '''



@route('/log')
def history():
    log = print_log()
    #return template('history.tpl', history = log)
    return template('{{history}}',history = log)

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)
