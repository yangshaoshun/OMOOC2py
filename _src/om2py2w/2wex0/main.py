# -*- coding: utf-8 -*-
'''文件说明:极简日志系统-桌面版
作者信息：yangshaoshun
版本自述：v1.3
更新：添加了滚动条，解决了内容超过显示框不自动跟随的问题
待解决问题1：因为 idle 编码问题，mac下无法输入中文 （windows下可以运行，tk版本为8.5 python为2.7.1）
待解决问题2：不止输入一行字符，使用 txt 输入一段文字，甚至可以输入 md 格式，下面展示转换后的内容
代办事项：书写 readme.md
代办事项2：docopt 的使用
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
master.title('MydailyTk')

w = Label(master, text = '^--^')
w.pack()

#提示信息:编辑某某文件
#headname = StringVar()
#w = Label(master, textvariable = headname)
#w = Label(master, text = '^--^')
#headname.set('编辑' + filename +'.txt')
#w.pack()

#通过按钮读取输入的内容，保存到本地文件中
def callback(*args):   # *args 的具体含义不知道，不加的话，提示 callback() takes no arguments
    txt = v.get()
    #target = open(filename + '.txt', 'a')
    target = open('mydaily.log', 'a')
    target.write(txt + '\n')
    target = open('mydaily.log')
    #s.set(target.read())  message模块使用
    with open('mydaily.log') as f:
        for line in f:
            lastline = line
    e.delete(0, END)
    e.focus_set()
    t.insert(END, lastline)
    t.see(END)   # 如果index指示的位置不可见，则滚动屏幕直至可见，写文本编辑器必备啊

#输入框
v = StringVar()
e = Entry(master, textvariable = v , width=50)
e.bind('<Return>',callback)
e.pack(fill="x")

#最早的Get按钮
#b = Button(master, text="get", width=10, command=callback)
#b.pack()

#通过 message 读取文件内容
#s = StringVar()
#target = open('mydaily.log')
#s.set(target.read())
#展示文件内容
#w = Message(master, textvariable=s, width=50)
#w.pack()

#添加滚动条
scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

t = Text(master, width = 30, wrap=WORD, yscrollcommand=scrollbar.set)
t.pack(anchor = W)
#设置一个标签，叫做 当前行为灰色
t.tag_config("endl", background="gray")
#t.bind("<Return>", highlightline)
with open('mydaily.log') as f:
    for line in f:
        t.insert(END, line)
        lastline = line
t.tag_add('endl', "current linestart", "current lineend+1c")
t.see(END) #如果index指示的位置不可见，则滚动屏幕直至可见，写文本编辑器必备啊

scrollbar.config(command=t.yview)

bu = Button(master, text = 'quit', command = master.quit) #退出按钮，添加成功
bu.pack(side=LEFT)

mainloop()