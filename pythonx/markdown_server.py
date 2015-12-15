#!/usr/bin/python
import socket
import signal
import errno
import markdown_parser
import markdown_preview
import threading
import markdown_lib
import sys
import httplib

class Server(threading.Thread):

    def Response(self, header, content):
        response = "%s %d\r\n\r\n%s\r\n\r\n" % (header, sys.maxint, content)
        return response

    def sigIntHander(self, signo, frame):
        self.isRun
        self.isRun = False
        self.lisfd.shutdown(socket.SHUT_RD)

    def __init__(self, port):
        self.PORT = port
        self.HOST = "localhost"
        threading.Thread.__init__(self)
        self.lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.lisfd.bind((self.HOST, self.PORT))
        self.lisfd.listen(2)
        signal.signal(signal.SIGINT, self.sigIntHander)

    def run(self):
        self.startServer()

    def startServer(self):
        header = "HTTP/1.1 200 OK\r\nContext-Type: text/html\r\nAccess-Control-Allow-Origin: *\r\nServer: Python-slp version 1.0\r\nContext-Length: "
        self.isRun = True
        while self.isRun:
            try:
                confd,addr = self.lisfd.accept()
            except socket.error as e:
                continue

            if self.isRun == False:
                break;

            content = markdown_preview.getBuff()
            markdown_lib._print(content)
            confd.send(self.Response(header, content))
            confd.close()

    def endServer(self):
        self.isRun = False
        conn = httplib.HTTPConnection("localhost:"+str(self.PORT))
        conn.request('GET', '/')
        self.lisfd.shutdown(socket.SHUT_RD)
        self.lisfd.close()
