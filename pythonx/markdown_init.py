#!/usr/bin/env python
# encoding: utf-8
import os
import vim
import platform
import shutil
import markdown_version


def init():
    if vim.eval("exists('g:MarkDownResDir')") == '1':
        DisResDir = vim.eval('g:MarkDownResDir')
    else:
        if platform.system() == 'Windows':
            DisResDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownRes')
        elif vim.eval("has('nvim')") == '1':
            DisResDir = os.path.join(vim.eval('$HOME'), '.nvim', 'MarkDownRes')
        else:
            DisResDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownRes')

    if vim.eval("exists('g:SourceMarkDownResDir')") == '1':
        SourceResDir = vim.eval('g:SourceMarkDownResDir')
    else:
        if platform.system() == 'Windows':
            SourceResDir = os.path.join(vim.eval('$HOME'), '.vim', 'bundle/markdown-preview.vim/resources')
        elif vim.eval("has('nvim')") == '1':
            SourceResDir = os.path.join(vim.eval('$HOME'), '.nvim', 'bundle/markdown-preview.vim/resources')
        else:
            SourceResDir = os.path.join(vim.eval('$HOME'), '.vim', 'bundle/markdown-preview.vim/resources')

    if not os.path.isdir(DisResDir) or not os.path.isfile(os.path.join(DisResDir, markdown_version.__PLUGIN_VERSION__)):
        if os.path.isdir(DisResDir):
            shutil.rmtree(DisResDir)
            print 'updating markdown-preview plugin...'

        shutil.copytree(SourceResDir, DisResDir)

        open(os.path.join(DisResDir, markdown_version.__PLUGIN_VERSION__), "w")

        print 'markdown-preview plugin has been updated to the lastest version: ' + markdown_version.__PLUGIN_VERSION__

    return False
