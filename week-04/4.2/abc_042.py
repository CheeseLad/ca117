#!/usr/bin/env python3

import sys

numbers = sys.stdin.readline().rstrip().split()
letterinput = sys.stdin.readline().rstrip()
numbers = sorted([int(n) for n in numbers])
numbers = [str(n) for n in numbers]
letters = "ABCDEF"
dict = dict(zip(letters, numbers))

print(" ".join([dict[char] for char in letterinput]))
