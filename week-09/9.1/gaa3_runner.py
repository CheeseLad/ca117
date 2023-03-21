from gaa_add_091 import Score

def main():

    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(1, 1)

    s5 = s3 + s4
    print(s5)
    assert(isinstance(s5, Score))
    assert(s5 is not s3)
    assert(s5 is not s4)

    before = s2
    s2 += s4
    print(s2)
    assert(isinstance(s2, Score))
    assert(s2 is before)
    assert(s2 is not s4)

if __name__ == '__main__':
    main()
