#!/usr/bin/env python

import socket

#tcp connection
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # connection to same port
s.bind(('0.0.0.0',8000))
s.listen(3)
(client, (ip, port))=s.accept()

print 'IP address of client is:', ip
print 'Port no of client is:' ,port

print 'client message'
client.recv(2048)

print 'server send message'

client.send('AH thik cha')

s.close()
