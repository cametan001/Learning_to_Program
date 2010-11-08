#! /usr/bin/env python
# -*- coding: utf-8 -*-

# GUI版ハングマン

# 作成者: A.J.Gauld
# 日付: 15-04-2000
from Tkinter import *
import hangman, string, sys

keys = [['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X'],
        ['Y', 'Z']]

# 値をコンストラクタへの引数として受け取る点以外は
# テキスト版と同じである
class hmGUIGuess(hangman.hmGuess):
    def __init__(self, ch):
        self.theValue = string.lower(ch)

# 多重継承を使う。このゲームクラスは、Tkinterの
# Frameオブジェクトの一種であると同時に、
# ハングマンゲームのサブクラスでもあるので、両方を継承する
class hmGUI(Frame, hangman.Hangman):
    def __init__(self, parent = 0):
        self.imgpath = ''               # プログラムとは別の場所に奥場合に設定する
        self.firstImg = self.imgpath + 'hm6.gif'
        self.letters = {}
        hangman.Hangman.__init__(self)
        Frame.__init__(self, 0)
        self.master.title("ハングマン")
        self.displayStart()

    # GUI版のゲームでは、GUIとその基盤となる
    # 各種ゲームオブジェクトをつなぐ部分において、
    # display()関数が多くの責務を持つ
    def display(self, chr):
        lossmsg = 'あなたの負けです! 正解:\n\t%s'
        playmsg = '当てる言葉: \n\t %s'
        successmsg = '正解! あなたの勝ちです。\nおめでとう。'
        # 一度提示された文字に印をつけておく
        self.letters[chr].config(state = DISABLED)
        # 推測を作成
        self.guesses.append(hmGUIGuess(chr))

        # 間違っていた場合に、挑戦できる残り回数を減らす
        self.outcome = self.theTarget.eval(self.guesses[-1])
        txt = self.getResult()
        if self.outcome > 0:                # まだプレイ中である
            if '_' not in txt:              # 正解が当てられた
                txt = successmsg
            else: txt = playmsg % self.getResult()
        else:
            txt = lossmsg % self.theTarget.getGoal()
        self.status.configure(text = txt)

        # イメージの更新
        thefile = self.imgpath + 'hm' + \
                  str(self.outcome) + '.gif'
        self.theImg.configure(file = thefile)

    def getTarget(self):
        return hangman.hmTarget()

    def play(self):
        self.mainloop()

    def quit(self):
        sys.exit()

    def reset(self):
        # 全ての文字に未提示の印をつける
        for l in string.uppercase:
            self.letters[l].config(state = ACTIVE)
        # 間違ってもよい回数と推測された文字のリストをリセットし、
        # 新しい正解を作成する
        self.outcome = 6
        self.guesses = []
        self.theTarget = self.getTarget()

        # イメージと現在の状態をリセットする
        self.theImg.configure(file = self.firstImg)
        txt = "当てる言葉:\n\t%s" % self.getResult()
        self.status.configure(text = txt)

    def displayStart(self):
        # 左半分に絵、右半分に文字盤が入った表示フレームを作成する
        # 絵はTextウィジェットに入れる
        d = Frame(self)
        hm = Text(d, relief = SOLID, width = 25, height = 17)
        # Imageオブジェクトを作成
        self.theImg = PhotoImage(file = self.firstImg)
        # 1行目の先頭に挿入
        hm.image_create('1.0', image = self.theImg)
        hm.pack(side = LEFT, padx = 20)
        # 文字盤を作成
        ltr = Frame(d, border = 1, relief = SUNKEN)
        for row in keys:
            f = Frame(ltr)
            for ch in row:
                action = lambda x = ch, s = self: s.display(x)
                self.letters[ch] = Button(f, text = ch,
                                          width = 2,
                                          command = action)
                self.letters[ch].pack(side=LEFT)
                f.pack(pady = 1)
            ltr.pack(side=LEFT)
            d.pack()

        # 左端に現在の状態、中央に [リセット]ボタン、
        # 右恥に [終了] ボタンを表示する制御フレームを作成する
        c = Frame(self, border = 1, relief = RAISED,
                  background = 'blue')
        txt = "当てる言葉: \n\t%s" % self.getResult()
        self.status = Label(c, anchor = W,
                            background = 'blue', foreground = 'yellow',
                            width = 25, text = txt)
        self.status.pack(side = LEFT, anchor = W)

        r = Button(c, text = 'リセット', padx = 10,
                   command = self.reset)
        r.pack(side = LEFT, padx = 10, pady = 5, anchor = W)

        q = Button(c, text = '終了', padx = 10, command = self.quit)
        q.pack(side = RIGHT, padx = 20, pady = 5, anchor = W)

        c.pack()
        self.pack()

if __name__ == "__main__":
    hmGUI().play()




















