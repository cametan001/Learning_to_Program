# -*- coding: utf-8 -*-

try:
    print "tryブロック開始"
    for i in [1, 2, 3]:
        print i/0                       # 0で除算!
    print "tryブロック終了"
except:                                 # 発生したエラーがあればトラップする
    print "エラー発生"
    i = 0                               # エラーを修正する間違ったアプローチ
    print i/0                           # 0による除算で、新たな例外が発生
