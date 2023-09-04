#!/usr/bin/env python3

import sys

def main():

  input_num = int(sys.stdin.readline().strip())

  magic_num = 0
  power = 0 # Multiplies the magic number by 10 to the power of this number and increases each cycle
  while input_num > 0: # Program works backwards from the number given
    input_num = input_num - 1
    # Either 3 or 9 is used depending on whether the number supplied is odd or even at the given time
    if input_num % 2 != 0: # odd
      magic_num = magic_num + 9 * (10 ** power)
    elif input_num % 2 == 0: # even
      magic_num = magic_num + 3 * (10 ** power)
    
    power = power + 1
    input_num = input_num // 2 # Divides number by 2 each time, until eventually the number will be less than or equal to zero, then the number will be printed

  print(magic_num)

if __name__ == "__main__":
    main()
