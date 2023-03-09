from student_082 import Student

def main():

    s1 = Student(15234654, 'Jimmy Murphy')

    assert(s1.name == 'Jimmy Murphy')
    assert(s1.sid == 15234654)
    assert(s1.modlist == [])
    s1.add_module('CA116')
    s1.add_module('CA117')
    print(s1)

    s2 = Student(17234654, 'Harry Byrne', ['CA177', 'CA101'])
    print(s2)

    s3 = Student(19343112, 'Mindy Malone')
    print(s3)

if __name__ == '__main__':
    main()
