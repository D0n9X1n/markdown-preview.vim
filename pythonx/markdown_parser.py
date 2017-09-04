#!/usr/bin/env python
# encoding: utf-8

import sys
import CommonMark
from imp import reload

try:
    reload(sys)
    sys.setdefaultencoding("utf-8")
except Exception as e:
    pass

def markdown(text, escape=True):
    parser = CommonMark.Parser()
    ast = parser.parse(text)

    renderer = CommonMark.HtmlRenderer()
    html = renderer.render(ast)
    return html
