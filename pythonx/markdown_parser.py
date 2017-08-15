#!/usr/bin/env python
# encoding: utf-8

import sys
import markdown2

reload(sys)
sys.setdefaultencoding("utf-8")

def markdown(text, escape=True):
    return markdown2.markdown(text);
    #  parser = CommonMark.Parser()
    #  ast = parser.parse(text)
    #  renderer = CommonMark.HtmlRenderer()
    #  html = renderer.render(ast)
    #  return html
