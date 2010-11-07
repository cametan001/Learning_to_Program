# -*- coding:utf-8 -*-

import string
def numwords(s):
    # splitがstringモジュールの関数であることを示さなければならない
    list = string.split(s)
    return len(list)                    # リスト内の要素の数を返す

inp = open("Learning_to_Program/The_Basics/Chapter12/menu.txt", "r")
total = 0                               # 0で初期化。これにより、変数が作成される

for line in inp.readlines():
    # 各業の単語数を足していく
    total += numwords(line)
print "このファイルの単語数は、%s語です。" % total

inp.close()
