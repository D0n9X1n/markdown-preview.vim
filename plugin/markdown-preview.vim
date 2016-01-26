""""""""""""""""""""""""""""""""""""""""""""
" let VERSION = '2.0.0'
" let AUTHOR  = 'Mike Tang'
" let EMAIL   = 'mikecoder.cn@gmail.com'
""""""""""""""""""""""""""""""""""""""""""""
if !has('python')
    echo 'Error: Required vim compile with +python'
    finish
endif

if(has("win32") || has("win64") || has("win95") || has("win16"))
    let g:iswindows = 1
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

function! MarkdownPath()
python << EOF
import vim, os, sys
sourced_file = vim.eval('s:SourcedFile')
while not os.path.exists(os.path.join(sourced_file, 'pythonx')):
    sourced_file = os.path.dirname(sourced_file)
module_path = os.path.join(sourced_file, 'pythonx')
sys.path.append(module_path)
EOF
endfunction

" Expand our path
let s:SourcedFile=expand("<sfile>")
call MarkdownPath()

function! MarkdownPreviewInit()
python << EOF
import markdown_init
markdown_init.init()
EOF
endfunction

call MarkdownPreviewInit()

function! LiveMarkdownPreviewStart()
python << EOF
import markdown_preview
markdown_preview.liveMarkdownPreviewStart()
EOF
endfunction

function! LiveMarkdownPreviewEnd()
python << EOF
import markdown_preview
markdown_preview.liveMarkdownPreviewEnd()
EOF
call ClearAll()
endfunction

function! MarkdownPreviewWithCustomCodeStyle(args1, args2)
python << EOF
import markdown_preview
markdown_preview.markdownPreviewWithCustomCodeStyle()
EOF
endfunction

function! MarkdownPreviewWithDefaultCodeStyle(args1)
python << EOF
import markdown_preview
markdown_preview.markdownPreviewWithDefaultCodeStyle()
EOF
endfunction

function! ClearAll()
python << EOF
import os, commands
currentpath = commands.getstatusoutput("pwd")[1]
try:
    os.remove(os.path.join(currentpath, 'tmp.html'))
except Exception:
    print ""
EOF
endfunction

function! PreviewWithDefaultCodeStyle(args1)
    call MarkdownPreviewWithDefaultCodeStyle(a:args1)
    if g:iswindows == 0
        !read ENTER
    endif
    call ClearAll()
endfunction

function! PreviewWithCustomCodeStyle(args1, args2)
    call MarkdownPreviewWithCustomCodeStyle(a:args1, a:args2)
    if g:iswindows == 0
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

map <leader>m :MarkdownPreviewWithCustomCodeStyleCodeStyle Github zenburn<CR>
if !exists(':LiveMarkdownPreviewStart')
    command -nargs=0 LiveMarkdownPreviewStart call LiveMarkdownPreviewStart()
endif

if !exists(':LiveMarkdownPreviewEnd')
    command -nargs=0 LiveMarkdownPreviewEnd call LiveMarkdownPreviewEnd()
endif

