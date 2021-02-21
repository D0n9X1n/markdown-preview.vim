#!/usr/bin/env python
# encoding: utf-8

import vim
import webbrowser
import os
import platform
import mistune


def markdown(text, escape=True):
    html = mistune.markdown(text, escape)
    return html


def markdownPreviewWithDefaultCodeStyle():
    cssName = vim.eval("a:args1")
    currentpath = os.getcwd()

    content = getHead(cssName)
    content += getBuff()
    content += getBody()

    file = open(os.path.join(currentpath, 'tmp.html'), 'w')
    file.write(content)
    file.close()

    url = 'file:///' + currentpath + '/tmp.html'
    webbrowser.open(url)


def markdownPreviewWithCustomCodeStyle():
    cssName = vim.eval("a:args1")
    codeName = vim.eval("a:args2")
    currentpath = os.getcwd()

    content = getHead(cssName, codeName)
    content += getBuff()
    content += getBody()

    file = open(os.path.join(currentpath, 'tmp.html'), 'w')
    file.write(content)
    file.close()

    url = 'file:///' + currentpath + '/tmp.html'
    webbrowser.open(url)


def getBuff():
    buff = ''
    for line in vim.current.buffer:
        buff += line + '\n'
    buff = markdown(buff, False)
    return buff


def getHead(cssStyle='github', codeStyle='default'):
    if vim.eval("exists('g:PluginDir')") == '1':
        resDir = os.path.join(vim.eval('g:PluginDir'), 'resources')
    else:
        resDir = os.path.join('markdown-preview.vim', 'resources')
        resDir = os.path.join('bundle', resDir)
        if platform.system() == 'Windows':
            resDir = os.path.join(vim.eval('$HOME'), '.vim', resDir)
        elif vim.eval("has('nvim')") == '1':
            resDir = os.path.join(vim.eval('$HOME'), '.nvim', resDir)
        else:
            resDir = os.path.join(vim.eval('$HOME'), '.vim', resDir)
        #  print(resDir)

    if cssStyle == '':
        cssStyle = 'github'
    if codeStyle == '':
        codeStyle = 'default'

    content = "<html>\n"
    content += '<meta charset="UTF-8" />\n'
    content += '<head>'
    content += '<style type="text/css"> svg { height:auto !important; } </style>\n'
    content += '<link rel="stylesheet" href="' + resDir + \
        '/code-styles/' + codeStyle.lower() + '.css">\n'
    content += '<link rel="stylesheet" href="' + \
        resDir + '/chart-styles/chart.css">\n'
    content += '<link href="' + resDir + '/' + \
        cssStyle.lower() + '.css" media="all" rel="stylesheet"/>\n'
    content += '<script src="' + resDir + '/js/highlight.min.js"></script>\n'
    content += '<script src="' + resDir + '/js/highlight.pack.js"></script>\n'
    content += '<script src="' + resDir + '/js/jquery-1.11.3.min.js"></script>\n'
    content += '<script src="' + resDir + '/js/mermaid.js"></script>\n'
    content += '<script> hljs.initHighlightingOnLoad(); window.onload = function() { mermaid.init({noteMargin: 5}, ".lang-chart"); mermaid.init({noteMargin: 5}, ".lang-mermaid"); }; </script>\n'
    content += '</head>\n<body id="content">'
    return content


def getBody():
    return "</body></html>\r\n\r\n\r\n\r\n"
