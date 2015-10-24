# -*- coding: utf-8 -*-

from sys import argv

#script, filename = argv

filename = raw_input(">>>Input your diary name: ")
target = open(filename + '.txt', 'a')

#review the history
#target = open(filename)
#print target.read()

#give some hint
print "You'are editing the %r file." % filename
print "Now you can write down your one-line journal."

#input

daily = raw_input(">>> ")
#回车键 ''
while daily != '' :    #有内容，继续；直接回车，保存退出
    target.write(daily)
    target.write('\n')
    daily = raw_input(">>> ")
    

#w,wirite mode
#r,read mode
#a,append mode


#write in srting and enter


#save file
print "保存文件..."
target.close()


#check the file again
#target_again = open(filename)
#print target_again.read()