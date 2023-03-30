#!/usr/bin/env python3

class Stack(object):
    
    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()
    
    def top(self):
        return self.l[len(self.l) - 1]
    
    def is_empty(self):
        return len(self.l) == 0
    
    def __len__(self):
        return len(self.l)

from math import sqrt

binops = {'+': float.__add__,
          '-': float.__sub__,
          '*': float.__mul__,
          '/': float.__truediv__}

uniops = {'n': float.__neg__,
          'r': sqrt}

def calculator(num):
    num = num.split()
    st = Stack()
    for n in num:
        if n not in binops and n not in uniops:
          st.push(float(n))
        elif n in binops:
          n1 = st.pop()
          n2 = st.pop()
          result = binops[n](n2, n1)
          st.push(result)
        elif n in uniops:
          binum = st.pop()
          result = uniops[n](binum)
          st.push(result)

    if len(st) == 1:    
      return st.top()

