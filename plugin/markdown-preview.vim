"""""""""""""""""""""""
" markdown-preview.vim
" version: v3.1.5
" author: Dongxin Tang
" mail: mike@mikecoder.cn
"""""""""""""""""""""""

if !(has('python') || has('python3'))
    echo 'Error: Required vim compile with +python or +python3'
    finish
endif

if has('python')
    let g:isPython3 = 0
endif

" we are prefer to use python3
if has('python3')
    let g:isPython3 = 1
endif

" check the os is windows, but we don't recommend to use this plugin on
" windows.
if(has("win32") || has("win64") || has("win95") || has("win16"))
    let g:iswindows = 1
    echo 'check the os is windows, but we do not recommend to use this plugin on windows.'
else
    let g:iswindows = 0
endif

" the target resource files folder
if !exists('g:MarkDownResDir')
    let g:MarkDownCSSDir='~/.vim/MarkDownRes'
endif

" the source resource files folder
if !exists('g:SourceMarkDownResDir')
    let g:SourceMarkDownCssDir='~/.vim/bundle/markdown-preview.vim/resources'
endif

" this is to define the path of the resource path
function! MarkdownPath()
    if g:isPython3
python3 << EOF
import vim, os, sys
sourced_file = vim.eval('s:SourcedFile')
while not os.path.exists(os.path.join(sourced_file, 'pythonx')):
    sourced_file = os.path.dirname(sourced_file)
module_path = os.path.join(sourced_file, 'pythonx')
sys.path.append(module_path)
EOF
    else
python << EOF
import vim, os, sys
sourced_file = vim.eval('s:SourcedFile')
while not os.path.exists(os.path.join(sourced_file, 'pythonx')):
    sourced_file = os.path.dirname(sourced_file)
module_path = os.path.join(sourced_file, 'pythonx')
sys.path.append(module_path)
EOF
    endif
endfunction

" Expand our path
let s:SourcedFile=expand("<sfile>")
" call MarkdownPath()

function! MarkdownPreviewWithCustomCodeStyle(args1, args2)
    if g:isPython3
python3 << EOF
import markdown_preview
markdown_preview.markdownPreviewWithCustomCodeStyle()
EOF
    else
python << EOF
import markdown_preview
markdown_preview.markdownPreviewWithCustomCodeStyle()
EOF
    endif
endfunction

function! MarkdownPreviewWithDefaultCodeStyle(args1)
    if g:isPython3
python3 << EOF
import markdown_preview
markdown_preview.markdownPreviewWithDefaultCodeStyle()
EOF
    else
python << EOF
import markdown_preview
markdown_preview.markdownPreviewWithDefaultCodeStyle()
EOF
    endif
endfunction

" clear all the temp files
function! ClearAll()
    if g:isPython3
python3 << EOF
import os
currentpath = os.getcwd()
try:
    os.remove(os.path.join(currentpath, 'tmp.html'))
except Exception:
    print("Delete auto create file " + currentpath + " error. Please delete it youself")
EOF
    else
python << EOF
import os
currentpath = os.getcwd()
try:
    os.remove(os.path.join(currentpath, 'tmp.html'))
except Exception:
    print("Delete auto create file " + currentpath + " error. Please delete it youself")
EOF
    endif
endfunction

function! PreviewWithDefaultCodeStyle(args1)
    call MarkdownPreviewWithDefaultCodeStyle(a:args1)
    if g:iswindows
        !pause
    else
        !read ENTER
    endif
    call ClearAll()
endfunction

function! PreviewWithCustomCodeStyle(args1, args2)
    call MarkdownPreviewWithCustomCodeStyle(a:args1, a:args2)
    if g:iswindows
        !pause
    else
        !read ENTER
    endif
    call ClearAll()
endfunction

if !exists(':MarkdownPreview')
    command -nargs=1 MarkdownPreview :call PreviewWithDefaultCodeStyle(<f-args>)
endif

if !exists(':MarkdownPreviewWithCustomCodeStyle')
    command -nargs=* MarkdownPreviewWithCustomCodeStyleCodeStyle call PreviewWithCustomCodeStyle(<f-args>)
endif

map <leader>m :MarkdownPreviewWithCustomCodeStyleCodeStyle GitHub solarized_light<CR>

