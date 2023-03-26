#!/usr/bin/env python 3

def minimum(lst, total=None):
    if total == None:
        total = lst[0]

    if len(lst) == 0:
        return total

    if lst[len(lst) - 1] < total:
        total = lst[len(lst) - 1]

    lst.pop()
    return minimum(lst, total)