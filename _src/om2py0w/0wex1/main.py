# -*- coding: gb2312 encoding -*-

from sys import argv

script, filename = argv

#review the history
target = open(filename)
print target.read()

#give some hint
print "You'are editing the %r file." % filename
print "Now you can write down your one-line journal."

#input
daily = raw_input("> ")

print daily

#w,wirite mode
#r,read mode
#a,append mode
target = open(filename, 'a')

#write in srting and enter
target.write(daily)
target.write("\n")

#save file
print "Saving the file..."
target.close()

raw_input("> ")

#check the file again
#target_again = open(filename)
#print target_again.read()