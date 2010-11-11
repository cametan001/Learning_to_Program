#! /usr/bin/env python
# -*- coding: utf-8 -*-

def print_table(multiplier):
    print "--- %dの掛け算表 ---" % multiplier
    for n in range(1, 13):
        print "%d×%d=%d" % (n, multiplier, n * multiplier)
