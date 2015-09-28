if !has('python')
    echo 'Error: Required vim compile with +python'
    finish
endif

let s:SourcedFile=expand("<sfile>")

function! MarkdownPreview(args1)
python << EOF
import vim
import mistune
import webbrowser
import shutil, os, platform
import commands

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
content += '<link crossorigin="anonymous" href="markdown.css" media="all" rel="stylesheet"/>'
buff = ''
for line in vim.current.buffer:
    buff += line + '\n'
content += mistune.markdown(buff)
content += "</html>"

print currentpath
file = open(currentpath+'tmp.html', 'w')
file.write(content)
file.close()

css = 'h1,h2,h3,h4,h5,h6,p,blockquote{margin:0;padding:0}body{font-family:"Helvetica Neue",Helvetica,"Hiragino Sans GB",Arial,sans-serif;font-size:13px;line-height:18px;color:#737373;background-color:white;margin:10px 13px 10px 13px}table{margin:10px 0 15px 0;border-collapse:collapse}td,th{border:1px solid #ddd;padding:3px 10px}th{padding:5px 10px}a{color:#0069d6}a:hover{color:#0050a3;text-decoration:none}a img{border:0;max-width:400px;max-height:400px}p{margin-bottom:9px}h1,h2,h3,h4,h5,h6{color:#404040;line-height:36px}h1{margin-bottom:18px;font-size:30px}h2{font-size:24px}h3{font-size:18px}h4{font-size:16px}h5{font-size:14px}h6{font-size:13px}hr{margin:0 0 19px;border:0;border-bottom:1px solid #ccc}blockquote{padding:13px 13px 21px 15px;margin-bottom:18px;font-family:georgia,serif;font-style:italic}blockquote:before{content:"\201C";font-size:40px;margin-left:-10px;font-family:georgia,serif;color:#eee}blockquote p{font-size:14px;font-weight:300;line-height:18px;margin-bottom:0;font-style:italic}code,pre{font-family:Monaco,Andale Mono,Courier New,monospace}code{background-color:#fee9cc;color:rgba(0,0,0,0.75);padding:1px 3px;font-size:12px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}pre{display:block;padding:14px;margin:0 0 18px;line-height:16px;font-size:11px;border:1px solid #d9d9d9;white-space:pre-wrap;word-wrap:break-word}pre code{background-color:#fff;color:#737373;font-size:11px;padding:0}sup{font-size:.83em;vertical-align:super;line-height:0}*{-webkit-print-color-adjust:exact}@media screen and (min-width:914px){body{width:854px;margin:10px auto}}@media print{body,code,pre code,h1,h2,h3,h4,h5,h6{color:black}table,pre{page-break-inside:avoid}}'
file = open(currentpath+'markdown.css', 'w')
file.write(css)
file.close()

url = 'file:///'+currentpath+'tmp.html'
webbrowser.open(url)
EOF
endfunction

function! ClearAll()
python << EOF
import vim
import shutil, os, platform

currentpath = commands.getstatusoutput("pwd")[1]
os.remove(currentpath+'tmp.html')
os.remove(currentpath+'markdown.css')

EOF
endfunction

function! Preview()
MarkdownPreview default
!read ENTER
ClearAll
endfunction

command! -nargs=1 MarkdownPreview :call MarkdownPreview(<f-args>)
command! -nargs=0 ClearAll :call ClearAll()
command! -nargs=0 Preview :call Preview()

map <leader>m :Preview<CR>



