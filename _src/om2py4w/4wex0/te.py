# -*- coding: utf-8 -*-
from bottle import * 

@route('/text')
def input():
    return'''
        <form action="/text" method="post">
        <p>请输入单行日记: <input type="text" name="fname" /></p>
        <input type="submit" value="确认" />
        </form>

    '''

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)
