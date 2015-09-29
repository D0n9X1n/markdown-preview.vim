#!/usr/bin/env python
# encoding: utf-8
import os, vim, platform, commands

def init():
    if vim.eval("exists('g:MarkDownCssDir')") == '1':
        cssDir = vim.eval('g:MarkDownCssDir')
    else:
        if platform.system() == 'Windows':
            cssDir = os.path.join(vim.eval('$HOME'), 'vimfiles', 'MarkDownCSS')
        elif vim.eval("has('nvim')") == '1':
            cssDir = os.path.join(vim.eval('$HOME'),'.nvim', 'MarkDownCSS')
        else:
            cssDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownCSS')

    if not os.path.exists(cssDir):
        print commands.getoutput('mkdir ' + cssDir)
        cssFile = "h1,\n" + "h2,\n" + "h3,\n" + "h4,\n" + "h5,\n" + "h6,\n" + "p,\n" + "blockquote {\n" + "    margin: 0;\n" + "    padding: 0;\n" + "}\n" + "body {\n" + "    font-family: \"Helvetica Neue\", Helvetica, \"Hiragino Sans GB\", Arial, sans-serif;\n" + "    font-size: 13px;\n" + "    line-height: 18px;\n" + "    color: #737373;\n" + "    background-color: white;\n" + "    margin: 10px 13px 10px 13px;\n" + "}\n" + "table {\n" + "    margin: 10px 0 15px 0;\n" + "    border-collapse: collapse;\n" + "}\n" + "td,th {\n" + "    border: 1px solid #ddd;\n" + "    padding: 3px 10px;\n" + "}\n" + "th {\n" + "    padding: 5px 10px;\n" + "}\n" + "\n" + "a {\n" + "    color: #0069d6;\n" + "}\n" + "a:hover {\n" + "    color: #0050a3;\n" + "    text-decoration: none;\n" + "}\n" + "a img {\n" + "    border: none;\n" + "    max-width:400px;\n" + "    max-height:400px;\n" + "}\n" + "p {\n" + "    margin-bottom: 9px;\n" + "}\n" + "h1,\n" + "h2,\n" + "h3,\n" + "h4,\n" + "h5,\n" + "h6 {\n" + "    color: #404040;\n"
        cssFile = cssFile + "    line-height: 36px;\n" + "}\n" + "h1 {\n" + "    margin-bottom: 18px;\n" + "    font-size: 30px;\n" + "}\n" + "h2 {\n" + "    font-size: 24px;\n" + "}\n" + "h3 {\n" + "    font-size: 18px;\n" + "}\n" + "h4 {\n" + "    font-size: 16px;\n" + "}\n" + "h5 {\n" + "    font-size: 14px;\n" + "}\n" + "h6 {\n" + "    font-size: 13px;\n" + "}\n" + "hr {\n" + "    margin: 0 0 19px;\n" + "    border: 0;\n" + "    border-bottom: 1px solid #ccc;\n" + "}\n" + "blockquote {\n" + "    padding: 13px 13px 21px 15px;\n" + "    margin-bottom: 18px;\n" + "    font-family:georgia,serif;\n" + "    font-style: italic;\n" + "}\n" + "blockquote:before {\n" + "    content:\"\\201C\";\n" + "    font-size:40px;\n" + "    margin-left:-10px;\n" + "    font-family:georgia,serif;\n" + "    color:#eee;\n" + "}\n" + "blockquote p {\n" + "    font-size: 14px;\n" + "    font-weight: 300;\n" + "    line-height: 18px;\n" + "    margin-bottom: 0;\n" + "    font-style: italic;\n" + "}\n" + "code, pre {\n" + "    font-family: Monaco, Andale Mono, Courier New, monospace;\n" + "}\n" + "code {\n" + "    background-color: #fee9cc;\n"
        cssFile = cssFile + "    color: rgba(0, 0, 0, 0.75);\n" + "    padding: 1px 3px;\n" + "    font-size: 12px;\n" + "    -webkit-border-radius: 3px;\n" + "    -moz-border-radius: 3px;\n" + "    border-radius: 3px;\n" + "}\n" + "pre {\n" + "    display: block;\n" + "    padding: 14px;\n" + "    margin: 0 0 18px;\n" + "    line-height: 16px;\n" + "    font-size: 11px;\n" + "    border: 1px solid #d9d9d9;\n" + "    white-space: pre-wrap;\n" + "    word-wrap: break-word;\n" + "}\n" + "pre code {\n" + "    background-color: #fff;\n" + "    color:#737373;\n" + "    font-size: 11px;\n" + "    padding: 0;\n" + "}\n" + "sup {\n" + "    font-size: 0.83em;\n" + "    vertical-align: super;\n" + "    line-height: 0;\n" + "}\n" + "* {\n" + "    -webkit-print-color-adjust: exact;\n" + "}\n" + "@media screen and (min-width: 914px) {\n" + "    body {\n" + "        width: 854px;\n" + "        margin:10px auto;\n" + "    }\n" + "}\n" + "@media print {\n" + "    body,code,pre code,h1,h2,h3,h4,h5,h6 {\n" + "        color: black;\n" + "    }\n" + "    table, pre {\n" + "        page-break-inside: avoid;\n" + "    }\n" + "}"
        print cssFile
        file = open(os.path.join(cssDir, 'default.css'), 'w+')
        file.write(cssFile)
        file.close()
