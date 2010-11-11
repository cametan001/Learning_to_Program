#! /usr/bin/env python
# -*- coding: utf-8 -*-

def numwords(s):
    list = split(s)                     # 単語が各要素となったリストを取得
    return len(list)                    # リストの要素数を返す

# for line in file:
#     # 各業の単語数を加算していく
#     total += numwords(line)
# print "このファイルの単語数は、%sです。" % total
