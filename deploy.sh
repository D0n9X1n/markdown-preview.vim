#!/bin/bash

# git add .
# git commit -am 'just in case'
# git push origin master
mv ~/.vim/bundle/markdown-preview.vim ~/markdown-preview.vim.back
cp -r ../markdown-preview.vim ~/.vim/bundle/markdown-preview.vim
