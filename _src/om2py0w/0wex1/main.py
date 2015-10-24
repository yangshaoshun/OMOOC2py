# -*- coding: utf-8 -*-

from sys import argv

#script, filename = argv

filename = raw_input(">>>Input your diary name: ")
target = open(filename, 'a')

#review the history
#target = open(filename)
#print target.read()

#give some hint
print "You'are editing the %r file." % filename
print "Now you can write down your one-line journal."

#input
daily = raw_input(">>> ")


#w,wirite mode
#r,read mode
#a,append mode


#write in srting and enter
target.write(daily)
target.write("\n")

#save file
print "Saving the file..."
target.close()

raw_input(">>> ")

#check the file again
#target_again = open(filename)
#print target_again.read()