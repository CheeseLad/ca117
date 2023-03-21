#!/usr/bin/env python3

from classlist_092 import Student, Classlist

def main():

    cl = Classlist()

    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    cl.add(s1)
    cl.add(s2)

    print(cl)


if __name__ == '__main__':
    main()
