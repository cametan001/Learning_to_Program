# -*- coding: utf-8 -*-

from bankaccount import *

# 標準のBankAccountのテスト
a = BankAccount(500)
b = BankAccount(200)
a.withdraw(100)
# a.withdraw(1000)
a.transfer(100, b)
print "A=", a.getBalance()              # 300になる
print "B=", b.getBalance()              # 300になる

# InterestAccountのテスト
c = InterestAccount(1000)
c.deposit(100)
print "C=", c.getBalance()               # 1133になる

# ChargingAccountのテスト
d = ChargingAccount(300)
d.deposit(200)
print "D=", d.getBalance()              # 500になる
d.withdraw(50)
print "D=", d.getBalance()              # 447になる
d.transfer(100, a)
print "A=", a.getBalance()              # 400になる
print "D=", d.getBalance()              # 344になる

# 最後に、ChargingAccountからInterestAccountに振込みする
# ChrgintAccountでは振り込み手数料が発送し、
# InterestAccountでは利息が発生する
print "C=", c.getBalance()              # 1133である
print "D=", d.getBalance()              # 344である
d.transfer(20, c)
print "C=", c.getBalance()              # 1187.59である
print "D=", d.getBalance()              # 321になる
