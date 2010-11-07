def printList(L):
    if L:
        print L[0]
        # [1:] については、Pythonのリファレンスマニュアルの
        # スライスの鉄名を参照のこと
        printList(L[1:])
