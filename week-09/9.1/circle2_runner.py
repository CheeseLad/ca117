from circle_add_091 import Point, Circle

def main():
    p1 = Point()
    p2 = Point(4, 6)

    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)

    c3 = c1 + c2
    assert(isinstance(c3, Circle))
    print(c3)

if __name__ == '__main__':
    main()
