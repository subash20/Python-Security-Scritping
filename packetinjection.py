#!/usr/bin/env python
import socket
import struct

rawsocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
rawsocket.bind(('wlp3s0',socket.htons(0x0800)))
newpkt=struct.pack('!6s6s2s','/xaa/xaa/xaa/xaa/xaa/xaa','/xbb/xbb/xbb/xbb/xbb/xbb','/x08/x00')
rawsocket.send(newpkt +"Hello world")


#print 'closing raw packet injection'

#rawsocket.close()
