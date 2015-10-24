'''
f = open('d1.txt')
for line in f:
    print line
f.close
'''

'''
with open('d1.txt') as f:
    for line in f:
        print line
f.close
'''

'''
filename = raw_input(">>> ")
#file = filename + '.txt'
#print file.read()
with open(filename + '.txt') as f:
	for line in f:
		print line
f.close()
'''
import os
filename = raw_input(">>> ")
fi= filename + '.txt'
print os.path.exists(fi)
#print file.read()
with open(fi) as f:
	for line in f:
		print line
f.close()

