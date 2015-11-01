import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    with open("mydaily.log") as f:
    	for line in f:
    		s.sendto(len(line),address)
    		s.sendto(line, address)
        if not line:
    	    break

#    msg = raw_input()
#    if not msg:
#        break
#    s.sendto(msg, address)

s.close()