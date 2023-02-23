#!/usr/bin/env python3

def arithmetic(p, q, r=5, s=2):
    return r - p + q + s

def main():

    print(arithmetic(1, 2, 5, 6))
# 5 - 1 + 2 + 6 = 12
    print(arithmetic(3, 4, 5))
# 5 - 3 + 4 + 2 = 8
    print(arithmetic(3, 4))
# 5 - 3 + 4 + 2 = 8
    print(arithmetic(3, 4, s=3))
# 5 - 3 + 4 + 3 = 9
    print(arithmetic(s=5, q=4, p=2, r=1))
# 1 - 2 + 4 + 5 = 8
    #print(arithmetic(q=2, p=4, 6))
# error
    #print(arithmetic(6, r=2, p=4))
# error
    print(arithmetic(p=2, q=4, s=6))
# 5 - 2 + 4 + 6 = 13
    #print(arithmetic(p=5, 2, 5))
#error

if __name__ == '__main__':
    main()
