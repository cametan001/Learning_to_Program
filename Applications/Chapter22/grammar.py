#! /usr/bin/env python
# -*- coding: utf-8 -*-

# モジュール:grammar
# 作成者:A.J. Gauld, 1999.8.19

# 機能:
# 散文体のテキストファイルの段落数、行数、センテンス数、
# 「文節数」、文字数、単語数、句読点数をカウントする。
# センテンスは、「.!?」のいずれかで終わるものとし、
# 段落は空白行で区切られるものとする。
# このプログラムでの「文節」とは、何らかの句読点で区切られた部分とする
# (このような定義では何の役にも立たないが、これは後ほど改良すればよいだろう)。

# 使い方:ファイル名をパラメータで受け取り、その全統計情報を出力する。
# 実際には、このファイル内の各関数は、セカンドモジュールから再利用して
# より便利なコマンドを提供するという目的で作成されている。

import string, sys

# グローバル変数の初期化
paragraph_count = 1             # 少なくとも１つの段落が存在することを前提としている！
line_count, sentence_count, clause_count, word_count = 0, 0, 0, 0
groups = []
alphas = string.letters + string.digits
stop_tokens = ['.', '?', '!']
punctuation_chars = ['&', '(', ')', '-', ';', ':', ','] + \
    stop_tokens
punctuation_counts = {}
for c in punctuation_chars:
    punctuation_counts[c] = 0
format = """ファイル %s の構成:
段落数:%d、 行数:%d、 センテンス数:%d
文節数:%d、 単語数:%d"""

# 処理を行う関数の定義
def getCharGroups(infile):
    global paragraph_count, line_count, groups
    try:
        for line in infile.readlines():
            line_count += 1
            if len(line) == 1:  # 改行のみの場合 => 段落区切り
                paragraph_count += 1
            else:
                groups += string.split(line)
    except:
        print "ファイルの読み取りに失敗しました。"
        sys.exit()

# def getPunctuation(wordList):
#     global punctuation_counts
#     for item in wordList:
#         while item and (item[-1] not in alphas):
#             p = item[-1]
#             item = item[:-1]
#             if p in punctuation_counts.keys():
#                 punctuation_counts[p] += 1
#             else:
#                 punctuation_counts[p] = 1

def getPunctuation(wordList):
    # 文字グループから句読点を取り除く
    for i in range(len(wordList)):
        wordList[i] = trim(wordList[i])
        # 空の単語を削除する
    for i in range(len(wordList)):
        if len(wordList[i]) == 0:
            del(wordList[i])
            
# def reportStats():
#     print format % (sys.argv[1],
#                     paragraph_count, line_count,
#                     sentence_count,
#                     clause_count, word_count)

def reportStats():
    global sentence_count, clause_count
    for p in stop_tokens:
        sentence_count += punctuation_counts[p]
    for c in punctuation_counts.keys():
        clause_count += punctuation_counts[c]
    print format % (sys.argv[1],
                    paragraph_count, line_count, sentence_count,
                    clause_count, len(groups))
    print "句読点文字の数:"
    for p in punctuation_counts.keys():print "\t%s\t:\t%3d" % (p, punctuation_counts[p])
    
# trim関数では、終了条件を0または-1とする再帰を使用する。
# -1、0、2以外の値が渡された場合にはInvalidEndエラーを発生させる。

def trim(item, end=2):
    """alphasに含まれない文字を左端(0)か右端(-1)、または
    その両方(2)から取り除く"""

    if end not in [-1, 0, 2]:
        raise "InvalidEnd"
    elif end == 2:
        item = trim(item, -1)           # まず右側を処理
        item = trim(item, 0)            # 次に左端を処理
    else:
        while (len(item) > 0) and (item[end] not in alphas):
            ch = item[end]
            if ch in punctuation_counts.keys():
                punctuation_counts[cd] += 1
            elif end == 0: item = item[1:]
            elif end == -1: item = item[:-1]
    return item

def Analyze(infile):
    getCharGroups(infile)
    getPunctuation(groups)
    reportStats()

# コマンドラインから呼び出された場合に実行する部分
# コマンドラインから呼び出されると、変数__name__が
# "__main__"に設定される
if __name__ == "__main__":
    if len(sys.argv) <> 2:
        print "使い方:python grammar.py <ファイル名>"
        sys.exit()
    else:
        Document = open(sys.argv[1], "r")
        Analyze(Document)
