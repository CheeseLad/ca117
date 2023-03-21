from schedule_092 import Meeting, Schedule

def main():
    schedule = Schedule()

    m = Meeting(13, 0, 15)
    schedule.add(m)

    m = Meeting(9, 5, 30)
    schedule.add(m)

    m = Meeting(16, 30, 5)
    schedule.add(m)

    print(schedule)

if __name__ == '__main__':
    main()
