#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        "simple Http server request handler"
        def do_GET(self):
                if self.path=='/admin':
                        self.wfile.write('this page is only for me admin')
                        self.wfile.write(self.headers)
                else:
                        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


server=SocketServer.TCPServer(('',6000),HttpHandler)

server.serve_forever()
