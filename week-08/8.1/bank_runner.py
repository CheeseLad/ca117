from bank_081 import BankAccount

def main():

    b1 = BankAccount()
    b1.set_attributes('Jim', 12343111, 300)

    assert(b1.name == 'Jim')
    assert(b1.number == 12343111)
    assert(b1.balance == 300)

    b1.print_attributes()
    b1.deposit(100)
    b1.print_attributes()

    assert(b1.balance == 400)


if __name__ == '__main__':
    main()
