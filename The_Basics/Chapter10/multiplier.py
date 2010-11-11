#! /usr/bin/env python
# -*- coding: utf-8 -*-

multiplier = input("乗数を入力してください : ")
for j in range(1, 13):
    print "%d×%d=%d" % (j, multiplier, j * multiplier)
