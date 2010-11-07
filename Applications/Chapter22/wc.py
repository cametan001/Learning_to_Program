#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, string

# コマンドラインまたはユーザ入力からファイル名を取得する
if len(sys.argv) < 2:
    name = raw_input('ファイル名を入力してください: ')
else:
    name = sys.argv[1]

inp = open(name, 'r')

# カウンタ変数を作成し、0で初期化する
words = 0
lines = 0
chars = 0

for line in inp.readlines():
    lines += 1
# １文を分割して単語のリストにし、単語数をカウントする
    list = string.split(line)
    words += len(list)
# 行内の文字数をカウントする
    chars += len(line)

fmtstr = "ファイル %s の構成は、 %d 行、 %d 単語、 %d 文字です。"
print fmtstr % (name, lines, words, chars)
inp.close()




















