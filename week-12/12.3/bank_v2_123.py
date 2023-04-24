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
        
    def __str__(self):
        rl = []
        ids = sorted(self.accounts)
        total = 0
        for id in ids:
            rl.append("Name: {}".format(self.accounts[id].name))
            rl.append("Number: {}".format(self.accounts[id].number))
            rl.append("Balance: {:.2f}".format(self.accounts[id].balance))
            total = total + self.accounts[id].balance

        rl.append("Total funds: {:.2f}".format(total))
        
        return "\n".join(rl)