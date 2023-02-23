#!/usr/bin/env python3

def append2list(l1, l2=None):
    if l2 == None:
      l2 = []

    for i in l1:
        l2.append(i)
    return l2
