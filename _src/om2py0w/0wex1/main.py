# -*- coding: utf-8 -*-
'''文件说明:极简日志系统
作者信息：yangshaoshun
版本自述：v1.0
    ...
'''
#全局引用
import time
import os

filename = raw_input(">>>Input your diary name: ")

#判断文件是否存在；存在，打印历史；不存在，新建。
if os.path.exists(filename + '.txt'):
    target = open(filename + '.txt', 'r')
    print target.read()
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
    elif line == 'h':
        print '''
        按 q/quit/Enter 推出
        按 h 查看帮助
        '''
    else:
	    wtime = time.strftime('%Y-%m-%d %H:%M:%S')
	    target.write(wtime + ' ' + line + '\n')
	    target.close()




#while (line != '') and (line != 'q') and (line !='quit'):    #有内容，继续；直接回车，保存退出
#    target.write(wtime + ' ' + line)
#    target.write('\n')
#    line = raw_input(">>> ")



#if __name__ == '__main__':
	#main()