VIM Markdown Preview
---

This is a vim markdown preview plugin.

####Installing

**Recommand Bundle or Vundle**

1. add `Bundle 'MikeCoder/markdown-preview.vim'` to your bundle file like vimrc or vimrc.bundle
2. and exec `BundleInstall` to install the plugin


> *Not Test Install Method*
>
> - then `vim plugin/markdown-preview.vim` to open the plugin file
>
> - use `source %`, to enable the plugin
>
> - use `<leader>m` to preview the markdown file in your default browser
>
> - or use `:MarkdownPreview` to preview your markdown docs

####Custom
this theme is in the css folder, if you want to change it to your favorite theme. follow the steps:

- go into your .vim folder
- find MarkDownCss folder and you will find default.css and GitHub.css here
- add your custom css file here, such as `exmaple.css`
- use vim open your markdown doc and `:MarkdownPreview example`
- and you will see your doc preview in your browser with example.css

####Thanks
1. mistune
2. vim

####LAST
wish you have a nice day

####LECENSE
see [@LECENSE](https://githu.com/MikeCoder/markdown-preview.vim/blob/master/LECENSE)

####TODO
see [@TODO.md](https://github.com/MikeCoder/markdown-preview.vim/blob/master/TODO.md)

####EXAMPLE
#####CODE TEST
```
import re
import inspect

__version__ = '0.7.1'
__author__ = 'Hsiaoming Yang <me@lepture.com>'
__all__ = [
    'BlockGrammar', 'BlockLexer',
    'InlineGrammar', 'InlineLexer',
    'Renderer', 'Markdown',
    'markdown', 'escape',
]


_key_pattern = re.compile(r'\s+')
_escape_pattern = re.compile(r'&(?!#?\w+;)')
_newline_pattern = re.compile(r'\r\n|\r')
_block_quote_leading_pattern = re.compile(r'^ *> ?', flags=re.M)
_block_code_leadning_pattern = re.compile(r'^ {4}', re.M)
_inline_tags = [
    'a', 'em', 'strong', 'small', 's', 'cite', 'q', 'dfn', 'abbr', 'data',
    'time', 'code', 'var', 'samp', 'kbd', 'sub', 'sup', 'i', 'b', 'u', 'mark',
    'ruby', 'rt', 'rp', 'bdi', 'bdo', 'span', 'br', 'wbr', 'ins', 'del',
    'img', 'font',
]
_pre_tags = ['pre', 'script', 'style']
_valid_end = r'(?!:/|[^\w\s@]*@)\b'
_valid_attr = r'''"[^"]*"|'[^']*'|[^'">]'''
_block_tag = r'(?!(?:%s)\b)\w+%s' % ('|'.join(_inline_tags), _valid_end)

```

#####IMAGE TEST
+ remote image 
    > ![Image Test](http://img3.douban.com/view/photo/photo/public/p2227609280.jpg)

+ local image 
    > ![Image Test](./images/Mike.jpg)



