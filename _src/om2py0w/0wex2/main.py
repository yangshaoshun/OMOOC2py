# -*- coding: utf-8 -*-
'''文件说明:极简日志系统-桌面版
作者信息：yangshaoshun
版本自述：v1.0
待解决问题1：因为 idle 编码问题，无法输入中文
待解决问题2：对文件的判断和操作，同时提示用户
待解决问题3：界面布局
待解决问题4：不止输入一行字符，使用 txt 输入一段文字，甚至可以输入 md 格式，下面展示转换后的内容
代办事项：书写 readme.md
代办事项2：docopt 的使用
'''
#全局引用
from Tkinter import *
from ttk import *
from sys import argv
reload(sys)
sys.setdefaultencoding( "utf-8" )

script, filename = argv

#开启窗口
master = Tk()

#提示信息
headname = StringVar()
w = Label(master, textvariable = headname)
w = Label(master, text = '^--^')
headname.set('编辑' + filename +'.txt')
w.pack()

#通过按钮读取输入的内容，保存到本地文件中
def callback(*args):   # *args 的具体含义不知道，不加的话，提示 callback() takes no arguments
    txt = v.get()
    target = open(filename + '.txt', 'a')
    target.write(txt + '\n')
    target = open(filename + '.txt')
    s.set(target.read())
    e.delete(0, END)
    e.focus_set()

#输入框
v = StringVar()
e = Entry(master, textvariable = v)
e.bind('<Return>',callback)
e.pack()

b = Button(master, text="get", width=10, command=callback)
b.pack()

#读取文件内容
s = StringVar()
target = open(filename + '.txt')
s.set(target.read())
#展示文件内容
w = Message(master, textvariable=s, width=500)
w.pack()

bu = Button(master, text = 'quit', command = master.quit) #退出按钮，添加成功
bu.pack()

mainloop()