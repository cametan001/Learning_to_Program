# -*- coding: utf-8 -*-

# あとから使うために例外文字列を作っておく。
BalanceError = "現在の口座残高は、 $%9.2f しかありません。"

class BankAccount:
    def __init__(self, initialAmount):
        self.balance = initialAmount
        print "口座を開設しました。口座残高は $%9.2f です。" % self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            raise BalanceError % self.balance

    def getBalance(self):
        return self.balance

    def transfer(self, amount, account):
        try:
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceError:
            print BalanceError

class InterestAccount(BankAccount):
    def deposit(self, amount):
        BankAccount.deposit(self, amount)
        self.balance = self.balance * 1.03

class ChargingAccount(BankAccount):
    def __init__(self, initialAmount):
        BankAccount.__init__(self, initialAmount)
        self.fee = 3

    def withdraw(self, amount):
        BankAccount.withdraw(self, amount+self.fee)
