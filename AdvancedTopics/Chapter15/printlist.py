# -*- coding: utf-8 -*-

def printList(L):
    # リストが空なら、何もしない
    if not L: return
    # 戦闘の項目の型がリストであれば、
    # 戦闘の項目を渡してprintListを呼び出す
    if type(L[0]) == type([]):
        printList(L[0])
    else:                               # リストでなければ、単純に先頭項目を表示する
        print L[0]
        # Lの残りの部分を処理する
    printList(L[1:])
