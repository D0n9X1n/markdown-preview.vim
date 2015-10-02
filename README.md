VIM Markdown Preview
---

This is a vim markdown preview plugin.

####Installing

**Recommand Bundle or Vundle**

1. add `Bundle 'MikeCoder/markdown-preview.vim'` to your bundle file like vimrc or vimrc.bundle
2. and exec `BundleInstall` to install the plugin

####Usage

1. edit your markdown doc normally
2. when you want to preview it in html you just use `:MarkdownPreview defult` to show your doc in your browser
3. if you want to change your style. you just use `:MarkdownPreview GitHub` in github style markdown view
4. you can also use `map <leader>m :MarkdownPreview GitHub<CR>` to have more fun

####Custom
this theme is in the css folder, if you want to change it to your favorite theme. follow the steps:

- go into your .vim folder
- find **MarkDownRes** folder and you will find default.css and GitHub.css here
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

### *中文文档版本*:[http://mikecoder.net/](http://mikecoder.net/?post=131)

####EXAMPLE

![Test Image](./images/image-test.png)

![Test Code](./images/code-test.png)

