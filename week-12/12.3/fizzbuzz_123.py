#!/usr/bin/env python3

import sys

nums = sys.stdin.readline().strip().split()

nums = [int(t) for t in nums]

for i in range(1, max(nums) + 1):
    if i % nums[0] == 0 and i % nums[1] != 0:
        print("fizz")
    if i % nums[0] != 0 and i % nums[1] == 0:
        print("buzz")
    if i % nums[0] == 0 and i % nums[1] == 0:
        print("fizzbuzz")
    elif i % nums[0] != 0 and i % nums[1] != 0:  
      print(i)