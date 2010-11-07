# -*- coding: utf-8 -*-

# 読み取るファイルを開く
imp = open("Learning_to_Program/The_Basics/Chapter12/menu.txt", "r")

# ファイル全体をリストに読み込み、各項目を表示する
for line in imp.readlines():
    print line

    # ファイルを閉じる
imp.close()
