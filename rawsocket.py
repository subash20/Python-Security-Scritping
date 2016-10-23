#!/usr/bin/env python

import socket
import struct
import binascii

rawPacket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))

pkt=rawPacket.recvfrom(2048)

etherHdr=pkt[0][0:14]
ipHdr=pkt[0][14:34]
tcp=pkt[0][34:54]

print 'Ethernet Packet Analysis !!!!!'
ethr=struct.unpack('!6s6s2s',etherHdr)
print 'Destination MAC address:',binascii.hexlify(ethr[0])
print 'Source MAC address:',binascii.hexlify(ethr[1])

print 'IP Header Packet Analysis!!!!'
ip_hdr=struct.unpack('!12s4s4s',ipHdr)
print 'Source IP adress:',socket.inet_ntoa(ip_hdr[1])
print 'Destination IP adress:',socket.inet_ntoa(ip_hdr[2])
                                                              1,1           Top
print 'TCP Header Analysis'

tcphdr=struct.unpack('!HH16s',tcp)
print 'destination port :',tcphdr[0]
print 'source port :',tcphdr[1]

