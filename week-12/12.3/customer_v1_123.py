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