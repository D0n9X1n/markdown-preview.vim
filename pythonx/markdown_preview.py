#!/usr/bin/env python
# encoding: utf-8

import vim
import markdown_parser
import webbrowser
import os, platform
import commands

def markdownPreview():
    cssName = vim.eval("a:args1")
    currentpath = commands.getstatusoutput("pwd")[1]

    if vim.eval("exists('g:MarkDownCssDir')") == '1':
        cssDir = vim.eval('g:MarkDownCssDir')
    else:
        if platform.system() == 'Windows':
            cssDir = os.path.join(vim.eval('$HOME'), 'vimfiles', 'MarkDownCSS')
        elif vim.eval("has('nvim')") == '1':
            cssDir = os.path.join(vim.eval('$HOME'),'.nvim', 'MarkDownCSS')
        else:
            cssDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownCSS')

    content = "<html>\n"
    content += '<meta charset="UTF-8" />'
    content += '<link href="' + cssDir + '/' + cssName + '.css" media="all" rel="stylesheet"/>'
    buff = ''
    for line in vim.current.buffer:
        buff += line + '\n'
    content += markdown_parser.markdown(buff)
    content += "</html>"

    print currentpath
    file = open(os.path.join(currentpath, 'tmp.html'), 'w')
    file.write(content)
    file.close()

    url = 'file:///' + currentpath + '/tmp.html'
    webbrowser.open(url)
