#!/usr/bin/python
import socket
import signal
import errno

def HttpResponse(header,whtml):
    context = 'hello world'
    response = "%s %d\n\n%s\n\n" % (header,len(context),context)
    return response

def sigIntHander(signo,frame):
    print 'get signo# ',signo
    global runflag
    runflag = False
    global lisfd
    lisfd.shutdown(socket.SHUT_RD)

strHost = "localhost"
HOST = strHost #socket.inet_pton(socket.AF_INET,strHost)
PORT = 20014

httpheader = '''''\
HTTP/1.1 200 OK
Context-Type: text/html
Server: Python-slp version 1.0
Context-Length: '''

lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lisfd.bind((HOST, PORT))
lisfd.listen(2)

signal.signal(signal.SIGINT,sigIntHander)

runflag = True
while runflag:
    try:
        confd,addr = lisfd.accept()
    except socket.error as e:
        if e.errno == errno.EINTR:
            print 'get a except EINTR'
        else:
            raise
        continue

    if runflag == False:
        break;

    print "connect by ",addr
    data = confd.recv(1024)
    if not data:
        break
    print data
    confd.send(HttpResponse(httpheader, 'index.html'))
    confd.close()
else:
    print 'runflag#', runflag

print 'Done'
