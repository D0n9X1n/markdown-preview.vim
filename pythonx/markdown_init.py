#!/usr/bin/env python
# encoding: utf-8
import os, vim, platform, commands, shutil, sys
import markdown_version

def init():
    print 'init'
    if vim.eval("exists('g:MarkDownResDir')") == '1':
        DisResDir = vim.eval('g:MarkDownResDir')
    else:
        if platform.system() == 'Windows':
            DisResDir = os.path.join(vim.eval('$HOME'), 'vimfiles', 'MarkDownRes')
        elif vim.eval("has('nvim')") == '1':
            DisResDir = os.path.join(vim.eval('$HOME'),'.nvim', 'MarkDownRes')
        else:
            DisResDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownRes')

    if vim.eval("exists('g:SourceMarkDownResDir')") == '1':
        SourceResDir = vim.eval('g:SourceMarkDownResDir')
    else:
        if platform.system() == 'Windows':
            SourceResDir = os.path.join(vim.eval('$HOME'), 'vimfiles', 'bundle/markdown-preview.vim/resources')
        elif vim.eval("has('nvim')") == '1':
            SourceResDir = os.path.join(vim.eval('$HOME'),'.nvim', 'bundle/markdown-preview.vim/resources')
        else:
            SourceResDir = os.path.join(vim.eval('$HOME'), '.vim', 'bundle/markdown-preview.vim/resources')

    if not os.path.isdir(DisResDir) or not os.path.isfile(os.path.join(DisResDir, markdown_version.__PLUGIN_VERSION__)):
        if os.path.isdir(DisResDir):
            commands.getoutput('rm -rf ' + DisResDir)
            print 'updating markdown-preview plugin...'

        if platform.system() == 'Windows':
            # not test on windows
            print commands.getoutput('xcopy /E ' + SourceResDir + ' ' + DisResDir)
        else:
            print commands.getoutput('cp -R ' + SourceResDir + ' ' + DisResDir)

        open(os.path.join(DisResDir, markdown_version.__PLUGIN_VERSION__), "w")

        print 'markdown-preview plugin has updated'
