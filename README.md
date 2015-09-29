VIM Markdown Preview
---

This is a vim markdown preview plugin.

####Installing

**Recommand Bundle or Vundle**

1. add `Bundle 'MikeCoder/markdown-preview.vim'` to your bundle file like vimrc or vimrc.bundle
2. and exec `BundleInstall` to install the plugin

> *Not Test Install Method*
> 1. then `vim plugin/markdown-preview.vim` to open the plugin file
> 2. use `source %`, to enable the plugin
> 3. use `<leader>m` to preview the markdown file in your default browser
> 4. or use `:MarkdownPreview` to preview your markdown docs

####Custom
this theme is in the css folder, if you want to change it to your favorite theme. follow the steps.
1. go into your .vim folder
2. find MarkDownCss folder and you will find default.css and GitHub.css here
3. add your custom css file here, such as `exmaple.css`
4. use vim open your markdown doc and `:MarkdownPreview example`
5. and you will see your doc preview in your browser with example.css

####Thanks
1. mistune
2. vim

####LAST
wish you have a nice day

####LECENSE
see [@LECENSE](https://githu.com/MikeCoder/markdown-preview.vim/blob/master/LECENSE)

####TODO
see [@TODO.md](https://github.com/MikeCoder/markdown-preview.vim/blob/master/TODO.md)
