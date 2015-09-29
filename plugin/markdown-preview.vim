if !has('python')
    echo 'Error: Required vim compile with +python'
    finish
endif

" Expand our path
let s:SourcedFile=expand("<sfile>")
exec g:_uspy "import vim, os, sys"
exec g:_uspy "sourced_file = vim.eval('s:SourcedFile')"
exec g:_uspy "while not os.path.exists(os.path.join(sourced_file, 'pythonx')):
   \ sourced_file = os.path.dirname(sourced_file)"
exec g:_uspy "module_path = os.path.join(sourced_file, 'pythonx')"
exec g:_uspy "sys.path.append(module_path)"

function! MarkdownPreviewInit()
python << EOF
import markdown_init
markdown_init.init()
EOF
endfunction

if empty(glob('~/.vim/MarkDownCSS/default.css'))
    call MarkdownPreviewInit()
endif

function! MarkdownPreview(args1)
python << EOF
import markdown_preview
markdown_preview.markdownPreview()
EOF
endfunction

function! ClearAll()
python << EOF
import os, commands
currentpath = commands.getstatusoutput("pwd")[1]
os.remove(os.path.join(currentpath, 'tmp.html'))
EOF
endfunction

function! Preview(args1)
call MarkdownPreview(a:args1)
!read ENTER
call ClearAll()
endfunction

command! -nargs=1 MarkdownPreview :call Preview(<f-args>)

map <leader>m :MarkdownPreview default<CR>
