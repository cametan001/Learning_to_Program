#! /usr/bin/env python
# -*- coding: utf-8 -*-

# モジュール:document.py
# 作成者:A.J. Gauld
# 日付:1999/08/26
# バージョン:1.0

# このモジュールは、さまざまな種類の文書(テキスト、HTML、LaTeXなど)用に
# サブクラス化することができるDocumentクラスを提供する。
# このファイルでは、テキストとごく基本的なHTML用のサブクラスの例を示す。

# このモジュールに含まれる主なサービスは次のとおりである。
# - getCharGroups()
# - getWords()
# - reportStats()
import sys, string, re

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.paragraph_count = 1
        self.line_count, self.sentence_count = 0, 0
        self.clause_count, self.word_count = 0, 0
        self.alphas = string.letters + string.digits
        self.stop_tokens = ['.', '?', '!']
        self.punctuation_chars = ['&', '(', ')', '-',
                                  ';', ':', ','] + \
                                  self.stop_tokens
        self.punctuation_counts = {}
        self.groups = []
        for c in self.punctuation_chars:
            self.punctuation_counts[c] = 0
        self.format = """ファイル %s の構成:
        段落数:%d、行数:%d、センテンス数:%d
        文節数:%d、単語数:%d\n"""

    def getCharGroups(self):
        try:
            f = open(self.filename, "r")
            for line in f.readlines():
                self.line_count += 1
                if len(line) == 1:          # 改行のみの場合 => 段落区切り
                    self.paragraph_count += 1
                else:
                    self.groups = self.groups+string.split(line)
        except:
            print "ファイルの読み取りに失敗しました。", self.filename
            sys.exit()

    def getWords(self):
        for i in range(len(self.groups)):
            self.groups[i] = self.ltrim(self.groups[i])
            self.groups[i] = self.rtrim(self.groups[i])
        self.removeExceptions()

    def removeExceptions():
        pass

    def ltrim(self, word):
        return word

    def rtrim(self, word):
        return word

    # def reportStats(self):
    #     pass

    def generateStats(self):
        self.word_count = len(self.groups)
        for c in self.stop_tokens:
            self.sentence_count += self.punctuation_counts[c]
        for c in self.punctuation_counts.keys():
            self.clause_count += self.punctuation_counts[c]

    def printStats(self):
        print self.format % (self.filename, self.paragraph_count,
                             self.line_count,
                             self.sentence_count,
                             self.clause_count,
                             self.word_count)
        print "句読点文字の数:"
        for i in self.punctuation_counts.keys():
            print "\t%s\t:\t%4d" % \
                  (i, self.punctuation_counts[i])

    def Analyze(self):
        self.getCharGroups()
        self.getWords()
        # self.reportStats()
        self.generateStats()

class TextDocument(Document):
    def ltrim(self, word):
        while (len(word) > 0) and \
              (word[0] not in self.alphas):
            ch = word[0]
            if ch in self.punctuation_counts.keys():
                self.punctuation_counts[ch] += 1
            word = word[1:]
        return word

    def rtrim(self, word):
        while (len(word) > 0) and \
              (word[-1] not in self.alphas):
            ch = word[-1]
            if ch in self.punctuation_counts.keys():
                self.punctuation_counts[ch] += 1
            word = word[:-1]
        return word

    def removeExceptions(self):
        top = len(self.groups)
        i = 0
        while i < top:
            if (len(self.groups[i]) == 0):
                del(self.groups[i])
                top -= 1
            else:
                i += 1

    def reportStats(self):
        self.word_count = len(self.groups)
        for c in self.stop_tokens:
            self.sentence_count += self.punctuation_counts[c]
        for c in self.punctuation_counts.keys():
            self.clause_count += self.punctuation_counts[c]

        print self.format % (self.filename,
                             self.paragraph_count,
                             self.line_count, self.sentence_count,
                             self.clause_count, self.word_count)
        print "句読点文字の数: "
        for i in self.punctuation_counts.keys():
            print "\t%s\t:\t%3d" % \
                  (i, punctuation_counts[i])

class HTMLDocument(Document):
    def getCharGroups(self):
        tag = re,complie("<.+?>")       # 欲張りな正規表現を使う
        para = re.compile("<[pP]>")     # 段落タグを検出する正規表現
        self.paragraph_count = 0        # 空の行ではなく<p>を使う
        try:
            f = open(self.filename, "r")
            lines = f.readlines()
            n = 0
            top = len(lines)
            while n < top:
                if len(lines[n]):        # 空白行でない場合
                    if para.search(lines[n]): # 段落￣が見つかった場合
                        self.paragragh_count += 1
                        lines[n] = tag.sub(' ', lines[n]) # タグを削除
                    elif len(lines[n]) <= 1:                # 空白行または'\n'のみ
                        del(lines[n])
                        top -= 1
                    else:
                        self.groups += string.split(lines[n])
                        n += 1
                else: n += 1
            self.line_count = len(lines)
        except:
            print "ファイルの読み取りに失敗しました。", self.filename
            sys.exit()

if __name__ == "__main__":
    if len(sys.argv) <> 2:
        print "使い方:python document.py"
        sys.exit()
    else:
        try:
            D = HTMLDocument(sys.argv[1])
            D.Analyze()
            D.printStats()
        except:
            print "ファイル %s の解析中にエラーが発生しました。" \
                  % sys.argv[1]
