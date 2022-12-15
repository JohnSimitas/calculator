from operators import mathmetical_operators

def calc():
    while True:
        print("""
            ---------------------
            |Available Operators|
            ---------------------
            |1) Addition +      |
            ---------------------
            |2) Subtraction -   |
            ---------------------
            |3) Division /      |
            ---------------------
            |4) Multiplication *|
            ---------------------
            |5) Power **        |
            ---------------------
        """)

        choice = input('Choose one of the available operators: ')

        while choice != '+' and choice != '-' and choice != '*' and choice != '/' and choice != '*' and choice != '**':
            add_again = input(f'The operator {choice} is not supported add one of the available operatos: ')

            if add_again == '+' or add_again == '-' or add_again == '*' or add_again == '/' or add_again == '**':
                break
        
        if choice == '**':
            num = int(input('Add a number: '))
            expo = int(input('Add the exposure: '))
            
            mathmetical_operators.power(num, expo)
            
            another_calc = input('Do you want to continue on other calculations? ')

            if another_calc == 'no':
                break
            else:
                continue

        num = int(input('Add the 1st number: '))
        num_2 = int(input('Add the 2nd number: '))

        if choice == '+':
            mathmetical_operators.addition(num, num_2)
        elif choice == '-':
            mathmetical_operators.subtraction(num, num_2)
        elif choice == '*':
            mathmetical_operators.multiplication(num, num_2)
        else:
            mathmetical_operators.division(num, num_2)

        another_calc = input('Do you want to do anoter calculation? ')
        
        if another_calc == 'yes':
            continue
        else:
            break


calc()