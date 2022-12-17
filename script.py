from operators import mathmetical_operators

def calc():
    while True:
        print("""
            |Available Operators    |
            |                       |
            |1) Addition +          |
            |                       |
            |2) Subtraction -       |
            |                       |
            |3) Division /          |
            |                       |
            |4) Multiplication *    |
            |                       |
            |5) Power **            |
            |                       |
            |6) Sqrt                |
        """)

        choice = input('Choose one of the available operators: ')

        while choice != '+' and choice != '-' and choice != '*' and choice != '/' and choice != '*' and choice != '**' and choice != 'Sqrt':
            add_again = input(f'The operator {choice} is not supported add one of the available operatos: ')

            if add_again == '+' or add_again == '-' or add_again == '*' or add_again == '/' or add_again == '**' or add_again == 'Sqrt':
                break
        
        
        if choice == '+':
            mathmetical_operators.addition()
        elif choice == '-':
            mathmetical_operators.subtraction()
        elif choice == '*':
            mathmetical_operators.multiplication()
        elif choice == '/':
            mathmetical_operators.division()
        elif choice == '**':
            mathmetical_operators.power()
        else:
            mathmetical_operators.square_root()

        another_calc = input('Do you want to make another calculation yes / no? ')

        if another_calc == 'yes':
            continue
        else:
            break

calc()
