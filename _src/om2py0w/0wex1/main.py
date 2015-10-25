# -*- coding: utf-8 -*-
'''文件说明:极简日志系统
作者信息：yangshaoshun
版本自述：v1.1
更新计划1：改成 main 函数的调用的形式；批量修改缩进(done)
更新计划2：然后使用 docopt，使得调用增加帮助、版本等常见参数
'''
#全局引用
import time
import os

#函数撰写区
def main():
    filename = raw_input(">>>Input your diary name: ")

    #判断文件是否存在；存在，打印历史；不存在，新建。
    if os.path.exists(filename + '.txt'):
        with open(filename + '.txt') as f:
            for line in f:
                print line,  #末尾有逗号，就不会自动换行
        target = open(filename + '.txt', 'a')
        
    else:
    	target = open(filename + '.txt', 'a')

    #give some hint
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
    	    target.close()

#自检区
if __name__ == '__main__':
	main()