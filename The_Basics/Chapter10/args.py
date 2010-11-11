#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
for item in sys.argv:
    print item
# argv[0]にはプログラム名が入っているため...
if len(sys.argv) > 1:
    print "最初の引数は : ", sys.argv[1]
