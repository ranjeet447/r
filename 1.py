from os import *
from __future__ import absolute_import


class BankAccount(object):

    default_acc_number = getenv("DEFAULT ACCOUNT NUMBER",1)
    def init (self, name, account_number, balance
    self.name = name
    self balance = balance
    self account number = account number
    Bank Account.default ach number Bank Account.default account number + 1


    def deposit(self, amount):
        deposited amount
        self.balance +amount
        self.balance += amount


    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough bal')
        else:
            self balance - amount

    def get_loan(self):
        raise NotImplemented
