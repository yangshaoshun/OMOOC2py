# -*- coding: utf-8 -*-
'''文件说明:极简日志系统-桌面版
作者信息：yangshaoshun
版本自述：v1.1
更新说明：使用 entry+message 的方式输入和展示笔记。记录保存在 mydiary.log 中

'''
#全局引用
from Tkinter import *
from ttk import *
from sys import argv
reload(sys)
sys.setdefaultencoding( "utf-8" )

#script, filename = argv

#开启窗口
master = Tk()
master.title('^--^')

#提示信息
#headname = StringVar()
#w = Label(master, textvariable = headname)
#w = Label(master, text = '^--^')
#headname.set('编辑' + filename +'.txt')
#w.pack()

#通过按钮读取输入的内容，保存到本地文件中
def callback(*args):   # *args 的具体含义不知道，不加的话，提示 callback() takes no arguments
    txt = v.get()
    target = open('mydiary.log', 'a')
    target.write(txt + '\n')
    target = open('mydiary.log')
    s.set(target.read())
    e.delete(0, END)
    e.focus_set()

#输入框
v = StringVar()
e = Entry(master, textvariable = v , width = 50)
e.bind('<Return>',callback)
e.pack()

b = Button(master, text="get", width=10, command=callback)
b.pack()

#读取文件内容
s = StringVar()
target = open('mydiary.log')
s.set(target.read())
#展示文件内容
w = Message(master, textvariable=s)
w.pack()

bu = Button(master, text = 'quit', command = master.quit) #退出按钮，添加成功
bu.pack(side = LEFT)

mainloop()