#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

# GUiとイベント処理メソッドを定義するアプリケーションクラスを作成
class KeysApp(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.txtBox = Text(self)
        # self.txtBox.bind("<Key>", self.doKeyEvent)
        # スペース文字を表すには'<space>'を使う
        # こうしなければ、Tkinterには空の文字列に見えてしまう
        self.txtBox.bind('<space>', self.doQuitEvent)
        self.txtBox.pack()
        self.pack()
    # def doKeyEvent(self, event):
    #     str = "%d\n" % event.keycode
    #     self.txtBox.insert(END, str)
    #     return "break"
    def doQuitEvent(self, event):
        import sys
        sys.exit()
# インスタンスを作成し、イベントループを開始する
myApp = KeysApp()
myApp.mainloop()
