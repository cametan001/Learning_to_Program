#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Message:
    def __init__(self, s = ''):
        self.txt = s

    def printIt(self):
        if self.txt == '':
            print 'メッセージなし'
        else:
            for i in range(3):
                print self.txt

m = Message('Hello World')
m.printIt()
