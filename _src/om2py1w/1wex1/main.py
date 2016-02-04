# -*- coding: utf-8 -*-

def main():
	print open('mydaily.log').read()
	while 1:
	    d = raw_input("当下>>>")
	    if d in ['q','quit']:
	    	break
	    elif d in ['?','help']:
	    	print '''
	    	?/help | help info
	    	q/quit | quit
	    	s/sync | sync the history 
	    	'''
	    elif d in ['s','sync']:
	    	print open('mydaily.log').read()
	    else:
	    	open('mydaily.log','a').write(d + '\n')

if __name__ == '__main__':
	main()