#! /usr/bin/env python
# -*- coding: utf-8 -*-

def times(n):
    for i in range(1, 13):
        print "%d×%d=%d" % (i, n, i * n)

print "7の掛け算表"
times(7)
