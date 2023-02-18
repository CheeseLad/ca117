#!/usr/bin/env python3

import sys

def main():
  line1 = sys.stdin.readline().rstrip()
  line2 = sys.stdin.readline().rstrip()
  line2backup = line2

  for i in range(len(line2)):
    if line1[i] == line2[i]:
      line2 = line2.replace(line2[i], "-", 1)
    else:
      line2 = line2.replace(line2[i], "*", 1)

  print(line1)
  print(line2backup)
  print(line2)

if __name__ == "__main__":
  main()
