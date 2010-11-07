# -*- coding: utf-8 -*-

try:
    print '１つ目のtry'
    try:
        print '２つ目のtry'
        print 'fred' ** 3               # TypeErrorを発生させる
    except TypeError:
        print 'TypeErrorが発生しました。'
        raise                           # この例外を１つ上のレベルに伝達する
except TypeError:
    print '今回は、ここでもエラー処理を行います。'
except:
    print '何らかの予想できないエラーが発生しました。'
