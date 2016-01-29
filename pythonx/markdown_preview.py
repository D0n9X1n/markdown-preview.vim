#!/usr/bin/env python
# encoding: utf-8
import socket
import vim
import markdown_parser
import webbrowser
import os, platform
import markdown_server
import markdown_lib

def markdownPreviewWithDefaultCodeStyle():
    cssName = vim.eval("a:args1")
    currentpath = os.getcwd()

    content = getHead(False, cssName)
    content += getBuff()
    content += getBody()

    file = open(os.path.join(currentpath, 'tmp.html'), 'w')
    file.write(content)
    file.close()

    url = 'file:///' + currentpath + '/tmp.html'
    webbrowser.open(url)

def markdownPreviewWithCustomCodeStyle():
    cssName     = vim.eval("a:args1")
    codeName    = vim.eval("a:args2")
    currentpath = os.getcwd()

    content = getHead(False, cssName, codeName)
    content += getBuff()
    content += getBody()

    file = open(os.path.join(currentpath, 'tmp.html'), 'w')
    file.write(content)
    file.close()

    url = 'file:///' + currentpath + '/tmp.html'
    webbrowser.open(url)

def checkPort():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind(('localhost', 20016))
    except Exception:
        return False
    return True

SERVER = None
def liveMarkdownPreviewStart():
    global SERVER
    if checkPort():
        SERVER = markdown_server.Server(20016)
        if not SERVER.isOK():
            print "Server is Wrong"
        else:
            SERVER.start()
            content = getHead(True)
            content += getBuff()
            content += getBody()
            currentpath = os.getcwd()
            file = open(os.path.join(currentpath, 'tmp.html'), 'w')
            file.write(content)
            file.close()
            url = 'file:///' + currentpath + '/tmp.html'
            webbrowser.open(url)
    else: print "Don't use the command twice, or you may not close the previous vim"

def liveMarkdownPreviewEnd():
    global SERVER
    try:
        SERVER.endServer()
    except Exception:
        print "Server is DOWN"

def getBuff():
    lineNum, curLineNum = 0, vim.current.window.cursor[0] - 1
    #  markdown_lib._print(curLineNum)
    buff = ''
    for line in vim.current.buffer:
        if lineNum == curLineNum:
            if line.startswith("```") or line.startswith('===') or line.startswith("---") or line == "":
                buff += line + '\n{ANCHOR}\n'
            else: buff += line + '{ANCHOR}\n'
        else: buff += line + '\n'
        lineNum = lineNum + 1
    buff = markdown_parser.markdown(buff)
    buff = buff.replace('{ANCHOR}', '<a id="anchor"></a>')
    return buff

def getHead(isLive = False, cssstyle = 'Github', codesytle = 'default'):
    if vim.eval("exists('g:MarkDownResDir')") == '1':
        cssDir = vim.eval('g:MarkDownResDir')
    else:
        if platform.system() == 'Windows':
            cssDir = os.path.join(vim.eval('$HOME'), 'vimfiles', 'MarkDownRes')
        elif vim.eval("has('nvim')") == '1':
            cssDir = os.path.join(vim.eval('$HOME'),'.nvim', 'MarkDownRes')
        else:
            cssDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownRes')

    content = "<html>\n"
    content += '<meta charset="UTF-8" />\n'
    content += '<head>'
    content += '<link rel="stylesheet" href="' + cssDir + '/code-styles/' + codesytle + '.css">\n'
    content += '<link href="' + cssDir + '/' + cssstyle + '.css" media="all" rel="stylesheet"/>\n'
    content += '<script src="' + cssDir + '/js/highlight.min.js"></script>\n'
    content += '<script src="' + cssDir + '/js/highlight.pack.js"></script>\n'
    content += '<script src="' + cssDir + '/js/jquery-1.11.3.min.js"></script>\n'
    content += '<script>hljs.initHighlightingOnLoad();</script>\n'
    if isLive == True:
        content += '<script src="' + cssDir + '/js/autoload.js"></script>\n'
    content += '</head>\n<body id="content">'
    return content

def getBody():
    return "</body></html>\r\n\r\n\r\n\r\n"
