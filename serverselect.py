from socket import *
import sys,select
SERVER_ADDR=('127.0.0.1',3000)
fd=socket(AF_INET,SOCK_DGRAM)
fd.bind(SERVER_ADDR)
while True:
	r=select.select([sys.stdin,fd],[],[])
	ready_list=r[0]
	for x in ready_list:
		if x is sys.stdin:
			s=raw_input()
			fd.sendto(s,CLIENT_ADDR)
		elif x is fd:
			s=x.recvfrom(1000)
			print s[0]
			CLIENT_ADDR=s[1]
