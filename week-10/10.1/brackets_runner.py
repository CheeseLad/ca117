from brackets_101 import matcher
import sys

tests = ['()',
'(())',
'(({}))',
'(())(){}{(([]))}',
'(()',
'(()){()]',
')(()){([()])}']

def main():

    for test in tests:
        print(matcher(test.strip()))

if __name__ == '__main__':
    main()