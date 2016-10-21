#!/usr/bin/env python

import sys,socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((sys.argv[1], 8000))

#s.listen(3)

while 1:
	userInput=raw_input('Please enter the string')
	s.send(userInput)
	print s.recv(2048)

s.close()
