#!/usr/bin/env python3

class BankAccount(object):

  def __init__(self, balance=0):
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance = self.balance - amount

  def __str__(self):
    return "Your current balance is {:.2f} euro".format(self.balance)
