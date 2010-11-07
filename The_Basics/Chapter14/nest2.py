# -*- coding: utf-8 -*-

try:
    print '１つ目のtry'
    try:
        print '２つ目のtry'
        print 'fred' ** 3               # TypeErrorを発生させる
    except TypeError:
        print 'TypeErrorが発生しました。'
except TypeError:
    print '決して表示されない'
except:
    print '何らかの予想できないエラーが発生しました。'
