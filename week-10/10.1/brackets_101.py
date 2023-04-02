#!/usr/bin/env python3

def matcher(line):
    num = 0
    if line.count("(") == line.count(")"):
        num = 1
    if line.count("{") == line.count("}"):
        num = num + 1
    if line.count("[") == line.count("]"):
        num = num + 1

    if num == 3:
        return True
    else:
        return False