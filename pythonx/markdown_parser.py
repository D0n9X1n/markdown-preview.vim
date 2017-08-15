#!/usr/bin/env python
# encoding: utf-8

import sys
import markdown_lib

reload(sys)
sys.setdefaultencoding("utf-8")

def markdown(text, escape=True):
    parser = markdown_lib.Markdown();
    return parser.convert(text);
