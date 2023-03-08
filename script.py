import operators

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

        while choice != '+' and choice != '-' and choice != '*' and choice != '/' and choice != '*' and choice != '**' and choice != 'sqrt':
            add_again = input(f'The operator {choice} is not supported add one of the available operatos: ')

            if add_again == '+' or add_again == '-' or add_again == '*' or add_again == '/' or add_again == '**' or add_again == 'sqrt':
        
                break
        
        
        if choice == '+':
            operators.addition()
        elif choice == '-':
            operators.subtraction()
        elif choice == '*':
            operators.multiplication()
        elif choice == '/':
            operators.division()
        
        elif choice == '**':
            operators.power()
        elif choice == 'sqrt':
            operators.square_root()
        else:
            operators.bmi()

        another_calc = input('Do you want to make another calculation yes / no? ')

        if another_calc == 'yes':
          
            continue
        else:
            break

calc()
