from contactlist_092 import Contact, Contactlist

def main():
    clist = Contactlist()

    c1 = Contact('Sue', '085-6442378', 'sue@eircom.net')
    clist.add(c1)

    c2 = Contact('Jimmy', '086-1223277', 'james@apple.com')
    clist.add(c2)

    c3 = Contact('Wendy', '086-9112645', 'wendy@physics.dcu.ie')
    clist.add(c3)

    c = clist.get('Wendy')
    assert(c is c3)

    clist.remove('Wendy')
    c = clist.get('Wendy')
    assert(c is None)

    c4 = Contact('Abbey', '087-7586344', 'abbey@gmail.com')
    clist.add(c4)

    print(clist)

if __name__ == '__main__':
    main()
