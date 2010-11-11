#! /usr/bin/env python
# -*- coding: utf-8 -*-

# -1が指定されたら、今日の曜日を表示する
def dayOfWeek(DayNum = -1):
    # 曜日のインデックスは、Pythonのローカル時間のタプル要素によって
    # 返される値に対応していなければならない(つまり、月曜日が0)
    days = ["月曜日", "火曜日",
           "水曜日", "木曜日",
           "金曜日", "土曜日", "日曜日"]

    # デフォルト値かどうかをチェック
    if DayNum == -1:
        # timeモジュールの関数を使って現在の時刻を取得する
        import time
        theTime = time.localtime(time.time())
        DayNum = theTime[6]             # 今日の曜日を取り出す
    return days[DayNum]
