#!/usr/bin/env python3

import sys

file = sys.argv[1]
dict = {}
filedetails = []

with open(file, "r") as f_in:
  for line in f_in:
    filedetails.append(line.strip())

for pair in filedetails:
  pair = pair.split()
  dict[pair[0]] = pair[1]


numbers = {"0" : "zero", "1" : "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "10" : "ten"}

for line in sys.stdin:
  line = line.strip().split()
  fin = " ".join([numbers[num] if num in numbers else "unknown" for num in line])
  fin = fin.split()
  print(" ".join([dict[nums] if nums in dict else "unknown" for nums in fin]))

