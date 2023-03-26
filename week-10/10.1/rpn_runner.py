from rpn_101 import calculator
import sys

tests = ['5',
'8.5 2 /',
'2 3 +',
'2 3 r +',
'1 2 3 * +',
'5 2 n *',
'1 2 3 + -',
'2 1 2 3 + - *',
'2 1 2 3 + - * n',
'2 1 2 3 + - * n r',
'6 +',
'9 r']

def main():

    for test in tests:
        try:
            a = calculator(test.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()