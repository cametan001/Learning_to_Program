# -*- coding: utf-8 -*-

# モジュールraiserr.py
def div42():
    denominator = input("42をいくつで割りますか？")
    if denominator == 0:
        raise ZeroDivisionError()
    else:
        return 42/denominator
