#!/usr/bin/env python
# encoding: utf-8

def _print(value = ''):
    logfile = open('all.log','a')
    logfile.write(value + '\n')
    logfile.flush()
    logfile.close()

