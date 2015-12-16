#!/usr/bin/python
import socket
import json
import signal
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
        self.isRun = False
        self.lisfd.shutdown(socket.SHUT_RD)

    def __init__(self, port):
        try:
            self.PORT = port
            self.HOST = "localhost"
            threading.Thread.__init__(self)
            self.lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.lisfd.bind((self.HOST, self.PORT))
            self.lisfd.listen(2)
            signal.signal(signal.SIGINT, self.sigIntHander)
        except Exception:
            print "the previous live preview may not close, only one live be allowed. if not, use killall -9 vim to kill the previous vim process"
            self.endServer()

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
            confd.send(self.Response(header, content))
            confd.close()

    def endServer(self):
        self.isRun = False
        try:
            conn = httplib.HTTPConnection("localhost:"+str(self.PORT))
            conn.request('GET', '/')
            self.lisfd.shutdown(socket.SHUT_RD)
            self.lisfd.close()
        except Exception:
            print "Markdown Server is Down"
