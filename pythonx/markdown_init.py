#!/usr/bin/env python
# encoding: utf-8
import os, vim, platform, commands, shutil

def init():
    if vim.eval("exists('g:MarkDownResDir')") == '1':
        DisResDir = vim.eval('g:MarkDownResDir')
    else:
        if platform.system() == 'Windows':
            DisResDir = os.path.join(vim.eval('$HOME'), 'vimfiles', 'MarkDownCSS')
        elif vim.eval("has('nvim')") == '1':
            DisResDir = os.path.join(vim.eval('$HOME'),'.nvim', 'MarkDownCSS')
        else:
            DisResDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownCSS')

    if vim.eval("exists('g:SourceMarkDownResDir')") == '1':
        SourceResDir = vim.eval('g:SourceMarkDownResDir')
    if not os.path.exists(SourceResDir):
        shutil.copytree(SourceResDir, DisResDir)


