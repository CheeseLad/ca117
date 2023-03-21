from point_091 import Point

def main():
    p1 = Point(2, 3)
    p2 = Point(4, 6)

    p3 = p1.midpoint(p2)

    print(p1)
    print(p2)
    print(p3)

    assert(isinstance(p3, Point))

if __name__ == '__main__':
    main()
