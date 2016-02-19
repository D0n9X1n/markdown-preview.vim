#!/usr/bin/env python
# encoding: utf-8

import markdown_version


def _print(value=''):
    if not markdown_version.__DEBUG__:
        return

    logfile = open('all.log', 'a')
    logfile.write(str(value) + '\n')
    logfile.flush()
    logfile.close()
