#!/usr/bin/env python
# encoding: utf-8

import vim
import markdown_parser
import webbrowser
import os, platform
import commands

def markdownPreviewWithDefaultCodeStyle():
    cssName = vim.eval("a:args1")
    currentpath = commands.getstatusoutput("pwd")[1]

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
    content += '<link rel="stylesheet" href="' + cssDir + '/code-styles/default.css">\n'
    content += '<link href="' + cssDir + '/' + cssName + '.css" media="all" rel="stylesheet"/>\n'
    content += '<script src="' + cssDir + '/js/highlight.min.js"></script>\n'
    content += '<script src="' + cssDir + '/js/highlight.pack.js"></script>\n'
    content += '<script>hljs.initHighlightingOnLoad();</script>\n'
    content += '</head>\n<body>'
    buff = ''
    for line in vim.current.buffer:
        buff += line + '\n'
    content += markdown_parser.markdown(buff)
    content += "</body></html>"

    print currentpath
    file = open(os.path.join(currentpath, 'tmp.html'), 'w')
    file.write(content)
    file.close()

    url = 'file:///' + currentpath + '/tmp.html'
    webbrowser.open(url)

def markdownPreviewWithCustomCodeStyle():
    cssName     = vim.eval("a:args1")
    codeName    = vim.eval("a:args2")
    currentpath = commands.getstatusoutput("pwd")[1]

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
    content += '<link rel="stylesheet" href="' + cssDir + '/code-styles/' + codeName + '.css">\n'
    content += '<link href="' + cssDir + '/' + cssName + '.css" media="all" rel="stylesheet"/>\n'
    content += '<script src="' + cssDir + '/js/highlight.min.js"></script>\n'
    content += '<script src="' + cssDir + '/js/highlight.pack.js"></script>\n'
    content += '<script>hljs.initHighlightingOnLoad();</script>\n'
    content += '</head>\n<body>'
    buff = ''
    for line in vim.current.buffer:
        buff += line + '\n'
    content += markdown_parser.markdown(buff)
    content += "</body></html>"

    print currentpath
    file = open(os.path.join(currentpath, 'tmp.html'), 'w')
    file.write(content)
    file.close()

    url = 'file:///' + currentpath + '/tmp.html'
    webbrowser.open(url)
