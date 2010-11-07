#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import document

## クラス定義
class GrammerApp(Frame):
    def __init__(self, parent = 0):
        Frame.__init__(self, parent)
        self.type = 2                   # デフォルト値を入れて変数を作成する
        self.master.title('ドキュメント解析')
        self.buildUI()

    def buildUI(self):
        # ファイル情報:ファイル名と種類
        fFile = Frame(self)
        Label(fFile, text = "ファイル名:").pack(side = "left")
        self.eName = Entry(fFile)
        self.eName.insert(INSERT, "test.htm")
        self.eName.pack(side = "left", padx = 5)

        # ラジオボタンの高さと名前を揃えるために、
        # 別のフレームが必要
        fType = Frame(fFile, borderwidth = 1, relief = SUNKEN)
        self.rText = Radiobutton(fType, text="テキストファイル",
                                 variable = self.type, value = 2,
                                 command = self.doText)
        self.rText.pack(side = TOP)
        self.rHTML = Radiobutton(fType, text="HTMLファイル",
                                 variable = self.type, value = 1,
                                 command = self.doHTML)
        self.rHTML.pack(side = TOP)
        # テキストファイルをデフォルトにする
        self.rText.select()
        fType.pack(side="right", padx = 3)
        fFile.pack(side = "top", fill = X)

        # 出力の表示にテキストボックスを使う。境界の余白も指定
        self.txtBox = Text(self, width = 60, height = 10)
        self.txtBox.pack(side = TOP, padx = 3, pady = 3)

        # 各処理の実行のためにコマンドボタンを使う
        fButtons = Frame(self)
        self.bAnalyze = Button(fButtons,
                               text = "解析",
                               command = self.AnalyzeEvent)
        self.bAnalyze.pack(side = LEFT, anchor = W, padx = 50, pady = 2)
        self.bReset = Button(fButtons,
                             text = "リセット",
                             command = self.doReset)
        self.bReset.pack(side = LEFT, padx = 10)
        self.bQuit = Button(fButtons,
                            text = "終了",
                            command = self.doQuitEvent)
        self.bQuit.pack(side = RIGHT, anchor = E, padx = 50, pady = 2)

        fButtons.pack(side = BOTTOM, fill = X)
        self.pack()

    ## イベント処理メソッド
    # プログラムを終了する
    def doQuitEvent(self):
        import sys
        sys.exit()

    # デフォルトの設定に戻す
    def doReset(self):
        self.txtBox.delete('1.0', END)
        self.rText.select()

    # ラジオボタンの選択状態を元に戻す
    def doText(self):
        self.type = 2

    def doHTML(self):
        self.type = 1

    # 適切な種類のドキュメントオブジェクトを作成し、その内容を解析する
    # 解析が終わったら、結果をフォームに表示する
    def AnalyzeEvent(self):
        filename = self.eName.get()
        if filename == "":
            self.txtBox.insert(END, "\nファイル名が指定されていません!\n")
            return
        elif self.type == 2:
            doc = document.TextDocument(filename)
        else:
            doc = document.HTMLDocument(filename)
            self.txtBox.insert(END, "\n解析中...\n")
        doc.Analyze()
        str = doc.format % (filename,
                            doc.paragraph_count, doc.line_count,
                            doc.sentence_count, doc.clause_count,
                            doc.word_count)
        self.txtBox.insert(END, str)

myApp = GrammerApp()
myApp.mainloop()
