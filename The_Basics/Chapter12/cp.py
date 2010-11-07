# -*- coding: utf-8 -*-

# 「cp menu.txt menu.bak」というコマンドと同じ処理を
# 行うプログラムを作成する
# まず読み取りモード(r)と書き込みモード(w)でファイルを開く
inp = open("Learning_to_Program/The_Basics/Chapter12/menu.txt", "r")
outp = open("Learning_to_Program/The_Basics/Chapter12/menu.bak", "w")

# eofに到達する(lineが偽になる)まで１行ずつファイルを読み取り、
# それを出力ファイルにコピーする
line = inp.readline()
while line:
    outp.write(line)
    line = inp.readline()
print "1つのファイルをコピーしました..."

# ファイルを閉じる
inp.close()
outp.close
