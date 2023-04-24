#!/usr/bin/env python3

class Customer(object):
    def __init__(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance

    def __str__(self):
        r = []
        r.append("Name: {}".format(self.name))
        r.append("Number: {}".format(self.number))
        r.append("Balance: {:.2f}".format(self.balance))
        return "\n".join(r)
    
class Bank(object):
    def __init__(self, accounts=None):
        if accounts == None:
            self.accounts = {}
        else:
            self.accounts = accounts

    def add(self, bank):
        self.accounts[bank.number] = bank

    def remove(self, num):
        if num in self.accounts:
            del(self.accounts[num])

    def lookup(self, num):
        if num in self.accounts:
            return self.accounts[num]
        elif num not in self.accounts:
            return None