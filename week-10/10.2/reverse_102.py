#!/usr/bin/env python3

def reverse(lst, newlist=None):
    if newlist == None:
        newlist = []
    if len(lst) > 0:
      newlist.append(lst.pop())
    if len(lst) == 0:
        tmp = newlist
        newlist = []
        return tmp

    return reverse(lst, newlist)
    