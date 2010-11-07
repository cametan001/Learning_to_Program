#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Game クラスは、全体の調整と表示を受け持つ
class Game:
    def __init__(self):
        self.theTarget = self.getTarget()
        self.GuessType = Guess
        self.outcome = 1
        self.guesses = []

    # メインの関数
    # 結果をチェックし、ゲームが終わっていれば処理を終了させる
    def play(self):
        self.displayStart()
        while (self.outcome):
            self.guesses.append(self.GuessType())
            self.outcome = self.theTarget.eval(self.guesses[-1])
            self.display(self.outcome)

    # 正しい種類の正解を生成するには、
    # このメソッドをオーバーライドしなければならない
    def getTarget(self):
        return Target()
    
    # リプレイ
    # 値を初期化し、最初の画面を再表示する
    def reStart(self):
        self.__init__()
        self.play()

    # プレイ方法の説明などの入ったオープニング画面を表示する
    def displayStart(self):
        print """
        抽象クラス: Game
        プレイするゲーム用のサブクラスのインスタンスを作成しなければなりません!"""

    # 結果に応じて適切な表示を行う
    def display(self, outcome):
        if outcome == 0:
            self.outcome = 0

# プレイヤーから値(推測)を受け取り、
# 評価に使われるデータを提供する
class Guess:
    def __init__(self):
        self.theValue = raw_input("何か入力してください: ")

    def value(self):
        return self.theValue

# プレイヤーに当てさせる正解のオブジェクトを生成する
# プレイヤーが提示した推測が辺りかどうかをチェックする
class Target:
    def __init__(self):
        self.goal = self.getTarget()

    def getTarget(self):
        return 0

    def getGoal(self):
        return self.goal

    def eval(self, aGuess):
        return 0

# 単純な言葉当てゲーム - フレームワークのテスト用
class NameGame(Game):
    names = ['Alan', 'fred', 'barney', 'heather', 'wilma', 'betty']
    def __init__(self):
        Game.__init__(self)
        self.failMsg = "残念、はずれ。もう一度挑戦してね！"
        self.successMsg = "おめでとう。 %d 回挑戦して、正解の %s を当てました。"
        self.theTarget = self.getTarget()
        self.GuessType = NameGuess      # クラス参照を変更
    def displayStart(self):
        print ("\n\n****************************")

    # Target ではなく NameTarget を取得するようにオーバーライドする
    def getTarget(self):
        return NameTarget()

    def display(self, outcome):
        Game.display(self, outcome)
        if outcome:
            print self.failMsg
        else:
            print self.successMsg % (len(self.guesses),
                                     self.theTarget.getGoal())

# 選択できる名前を表示し、デフォルトプロンプトを変更する
class NameGuess(Guess):
    def __init__(self):
        print NameGame.names
        self.theValue = raw_input("名前を入力してください: ")

# プレイヤーに名前を当てさせ、
# 正解になるまでの回数をカウントする
class NameTarget(Target):
    def getTarget(self):
        import random
        return NameGame.names[int(random.random() * \
                                  (len(NameGame.names) - 0.001))]

    def eval(self, aGuess):
        if self.goal == aGuess.value():
            return 0
        else:
            return 1

# ゲームオブジェクトを作成し、プレイを開始する
if __name__ == "__main__":
    mygame = NameGame()
    mygame.play()
    mygame.reStart()
