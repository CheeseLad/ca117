from meeting_092 import Meeting

def main():

    m = Meeting(9, 5, 30)

    assert(m.hour == 9)
    assert(m.minute == 5)
    assert(m.duration == 30)

    print(m)

if __name__ == '__main__':
    main()
