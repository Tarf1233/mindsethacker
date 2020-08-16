#!/usr/bin/python
import socket,sys
ports = 21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,2221,3306,3389,5900,8080
#for port in range (1,65535):
for port in ports:
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if not soc.connect_ex((sys.argv[1], port)):
		print "porta", port, "aberta"
		soc.close()
	port = port+1
