#!/usr/bin/env python3

def maximum(lst, total=0):
    if len(lst) == 0:
        return total

    if lst[len(lst) - 1] > total:
        total = lst[len(lst) - 1]

     
    lst.pop()
    return maximum(lst, total)
        