#! /usr/bin/env python
# -*- coding: utf-8 -*-

def isPositive(v):
    if v >= 0:
        return 1
    else:
        return 0

x = input('値を入力してください。')
if isPositive(x):
    print x, 'は、正の値です。'
