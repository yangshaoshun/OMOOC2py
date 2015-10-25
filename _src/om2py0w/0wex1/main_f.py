# -*- coding: utf-8 -*-
'''文件说明:极简日志系统
作者信息：yangshaoshun
版本自述：v1.1
更新计划1：改成 main 函数的调用的形式；批量修改缩进(done)
更新计划2：然后使用 docopt，使得调用增加帮助、版本等常见参数
'''
#全局引用
import os,time

#函数撰写区
def history(filename):
    if os.path.exists(filename + '.txt'):
        with open(filename + '.txt') as f:
            for line in f:
                print line

def writing(filename):
    target = open(filename + '.txt', 'a')
    print "You'are editing the %r file." % filename
    print "Now you can write down your one-line journal."

    while True:
        line = raw_input(">>> ")
        if line == 'q' or line == 'quit' or line == '':
            target.close()
            print "保存文件并推出..."
            break
        elif line == 'h' or line == '?' or line == 'help':
            print '''
            输入 q/quit/Enter 推出
            输入 ?/h/hlep 查看帮助
            '''
        else:
            wtime = time.strftime('%Y-%m-%d %H:%M:%S')
            target.write(wtime + ' ' + line + '\n')
       
def main():
    filename = raw_input(">>>Input your diary name: ")
    history(filename)
    writing(filename)
    
#自检区
if __name__ == '__main__':
    main()