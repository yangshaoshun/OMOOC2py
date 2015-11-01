import os

def main():
    filename = raw_input(">>> ")
    fi= filename + '.txt'
    print os.path.exists(fi)
    #print file.read()
    with open(fi) as f:
    	for line in f:
    		print line
    f.close()

if __name__ == '__main__':
	main()