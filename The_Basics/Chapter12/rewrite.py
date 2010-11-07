# -*- coding: utf-8 -*-

import os, time
try:
    # ファイルと変数の初期化
    menu = open('Learning_to_Program/The_Basics/Chapter12/menu.txt', 'r')
    outf = open('Learning_to_Program/The_Basics/Chapter12/menu.tmp', 'w')
    header = 'Menu for %s' % time.ctime(time.time())

    # ヘッダを書き込んでから、メニュー部分を追加する
    outf.write(header + '\n\n')
    lines = menu.readlines()
    for i in range(2, len(lines)):
        outf.write(lines[i])
    outf.close()
    menu.close()

    # ファイル処理
    os.rename('Learning_to_Program/The_Basics/Chapter12/menu.txt',\
              'Learning_to_Program/The_Basics/Chapter12/menu.bak')
    os.rename('Learning_to_Program/The_Basics/Chapter12/menu.tmp',\
              'Learning_to_Program/The_Basics/Chapter12/menu.txt')
    os.remove('Learning_to_Program/The_Basics/Chapter12/menu.bak')

except:
    print 'エラー:新しいメニューの作成に失敗しました。'
