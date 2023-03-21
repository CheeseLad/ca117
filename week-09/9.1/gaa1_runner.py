from gaa_091 import Score

def main():

    s1 = Score()
    print(s1)

    s2 = Score(3, 12)
    assert(s2.goals == 3)
    assert(s2.points == 12)
    print(s2)

if __name__ == '__main__':
    main()
