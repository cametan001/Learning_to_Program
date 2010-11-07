#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
# <とIの間に任意の数のスペースが入る場合も考慮して、
# IMGタグ(大文字または小文字のIMG)を探す
img = '< *[Ii][Mm][Gg] '
# >に到達するまでに現れるALT属性を探す
alt = img + '[^>]*[Aa][Ll][Tt].*>'
# ファイルを開いてリストに読み込む
filename = raw_input('チェックするHTMLファイルの名前: ')
inf = open(filename, 'r')
lines = inf.readlines()

# IMGタグがあって、タグ内にALTの見つからない行が見つかったら
# コメントに入れた警告メッセージを追加する
for i in range(len(lines)):
    if re.search(img, lines[i]) and not \
           re.search(alt, lines[i]):
        lines[i] = '<!-- 画像にはALT属性をつけること! -->\n' \
                   + lines[i]

# 変更後の内容をファイルに書き込み、ファイルを閉じる
inf.close()
outf = open(filename, "w")
outf.writelines(lines)
outf.close()
