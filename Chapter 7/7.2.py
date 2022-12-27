#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:54:02 2021

@author: Bard
"""
class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1
        
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1
        
    def dump(self):
        print("%s, %s, balance: %s, transactions: %d" % (self.name, self.no, self.balance, self.transactions))
        
    @staticmethod
    def test():
        a = Account("H.P.L.", "121344312", 1000)
        a.withdraw(3000)
        a.deposit(20)
        assert a.transactions == 2
        
Account.test()