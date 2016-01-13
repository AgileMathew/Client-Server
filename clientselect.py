from socket import *
import select,sys
SERVER_ADDR=('127.0.0.1',3000)
fd=socket(AF_INET,SOCK_DGRAM)
while True:
	r=select.select([sys.stdin,fd],[],[])
	ready_list=r[0]
	for x in ready_list:
		if x is sys.stdin:
			s=raw_input()
			fd.sendto(s,SERVER_ADDR)
		elif x is fd:
			s=x.recvfrom(1000)
			print s[0]
