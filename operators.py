"""OPERATORS MODULE
Operators Module is a module that calculates the simpliest mathematic operators
"""

from math import sqrt

<<<<<<< HEAD

def addition():
    """Takes 2 int numbers and finds the additions of them"""
    number = int(input('Add the 1st number: ')) 
    number_ = int(input('Add the 2nd number: '))
=======
class mathmetical_operators:
    def addition():
        number
        number_ = int(input('Add the 1st number: ')) 
        
        
        print(sum)
>>>>>>> 1d26c3f9e37a2e9144560905243a4d4c6d61a88c
    
    calc = number + number_
    
    print(calc)

def subtraction():
    """Takes 2 int numbers and finds the subtraction of them"""
    number = int(input('Add the 1st number: ')) 
    number_ = int(input('Add the 2nd number: '))
   
    calc = number - number_
     
    print(calc)

def multiplication():
        """Takes 2 int numbers and finds the multiplication of them"""
        number = int(input('Add the 1st number: ')) 
        number_ = int(input('Add the 2nd number: '))
       
        calc = number * number_
        
       
        print(calc)

def division():
        """Takes 2 int numbers and finds the division of them"""
        number = int(input('Add the 1st number: ')) 
        number_ = int(input('Add the 2nd number: '))
       
        calc = number / number_
       
        print(calc)

def power():
    """Takes 2 int numbers and finds the power of them"""
    number = int(input('Add the 1st number: ')) 
    expo = int(input('Add the exposure: '))

    calc = number ** expo
    
    print(calc)

<<<<<<< HEAD

def square_root():
    """Takes 1 int numbers and finds the square root of them"""
    x = int(input('Add the number: '))

    print(sqrt(x))

def bmi():
    """Takes the weight and the height and finds the BMI"""
    weight = int(input('Add your weight: '))
    height = float(input('Add your height: '))


    BMI = weight / height ** 2

    if BMI < 18.5:
        print('Your BMI is:',BMI,'underweight')
    elif BMI >= 18.5 and BMI <= 24.9:
        print(f'Your BMI is {BMI} normal weight')
    elif BMI >= 25.0 and BMI <= 29.9:
        print(f'Your BMI is {BMI} overweight')
    elif BMI >= 30.0 and BMI <= 34.9:
        print(f'Your BMI is {BMI} obesity class I')
    elif BMI >= 35.0 and BMI <= 39.9:
        print(f'Your BMI is {BMI} obesity class II')
    else:
        print(f'Your BMI is: {BMI} obesity class III')
=======
        print(sqrt(x))
>>>>>>> 1d26c3f9e37a2e9144560905243a4d4c6d61a88c
