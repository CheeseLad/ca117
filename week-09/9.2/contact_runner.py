from contact_092 import Contact

def main():

    c = Contact('Sue', '085-6442378', 'sue@eircom.net')

    assert(c.name == 'Sue')
    assert(c.phone == '085-6442378')
    assert(c.email == 'sue@eircom.net')

    print(c)

if __name__ == '__main__':
    main()
