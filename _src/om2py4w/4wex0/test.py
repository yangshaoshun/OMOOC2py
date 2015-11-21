# -*- coding: utf-8 -*-
from bottle import * # or route


@route('/hello')
def hello():
    return "Hello World!"

@route('/hello/<name>')
def hello(name):
    return "Hello World! %s" % name

@route('/')
@route('/text')
def input():
    return'''
        <form action="/text" method="post">
        <p>请输入单行日记: <input type="text" name="fname" /></p>
        <input type="submit" value="确认" />
        </form>

    '''

@route('/text', method ='POST')
def do_input():
    line = request.forms.get('fname')
    if line:
        return line


@route('/login') 
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username:
        return username

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)