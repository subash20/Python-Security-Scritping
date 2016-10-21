
#!/usr/bin/env python

import SocketServer

class Echohandler(SocketServer.BaseRequestHandler):
	"Echo client server class"
	def handle(self):
		print 'Client connection is ',self.client_address
		
		while 1:
			data=self.request.recv(2048) #request.recv same as socket.recv
			self.request.send(data)
		print 'client left'

serveradd=('0.0.0.0',9000)
server=SocketServer.TCPServer(serveradd,Echohandler)
  # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
server.serve_forever()
