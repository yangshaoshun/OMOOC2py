# -*- coding: utf-8 -*-
'''文件说明:极简日志系统-桌面版
作者信息：yangshaoshun
版本自述：v1.2
更新：本地必须是有 mydiary.log；使用 text 插件显示内容，不用输入文件名称；main_me.py 使用 message 插件显示内容
待解决问题1：因为 idle 编码问题，无法输入中文
待解决问题2：考虑使用 单行显示的text + message 输入和展示
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
    #target = open(filename + '.txt', 'a')
    target = open('mydiary.log', 'a')
    target.write(txt + '\n')
    target = open('mydiary.log')
    #s.set(target.read())
    with open('mydiary.log') as f:
        for line in f:
            lastline = line
    e.delete(0, END)
    e.focus_set()
    t.insert(END, lastline)
    #t.insert(END, lastline,'current_line')
    #t.tag_remove("current_line", 1.0, "end")

#输入框
v = StringVar()
e = Entry(master, textvariable = v , width=50)
e.bind('<Return>',callback)
e.pack(fill="x")

#b = Button(master, text="get", width=10, command=callback)
#b.pack()

#读取文件内容
#s = StringVar()
#target = open('mydiary.log')
#s.set(target.read())
#展示文件内容
#w = Message(master, textvariable=s, width=50)
#w.pack()

#def highlightline(Event=None):
#        t.tag_remove("current_line", 1.0, "end")
#        t.tag_add("current_line", "current linestart", "current lineend+1c")

t = Text(master, width = 30)
t.pack(anchor = W)
#设置一个标签，叫做 当前行为灰色
#t.tag_configure("current_line", background="gray")
#t.bind("<Return>", highlightline)
with open('mydiary.log') as f:
    for line in f:
        t.insert(END, line)
        lastline = line

bu = Button(master, text = 'quit', command = master.quit) #退出按钮，添加成功
bu.pack(side=LEFT)

mainloop()