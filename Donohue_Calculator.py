#Programmed by Sarah Donohue 
#10/29/22
#Donohue-Calculator.py
#this program will create an application that will calculate sums, differences, products or quotient of two numbers

calc = str(input('Please select one option: add/subract/multiply/divide: '))
try: 
    first_number = float(input('What is the first number? '))
    second_number = float(input('What is the second number? '))
except (NameError, ValueError):
    print('That is not a number!')

if calc.lower() == 'add':
    print('You chose add')
    outcome = first_number + second_number
    print(first_number, ' + ', second_number, ' = ', outcome)
elif calc.lower() == 'subtract':
    print('You chose subtract')
    outcome = first_number - second_number
    print(first_number, ' - ', second_number, ' = ', outcome)
elif calc.lower () == 'multiply':
    print('You chose multiply')
    outcome = first_number * second_number
    print(first_number, ' * ', second_number, ' = ', outcome)
elif calc.lower () == 'divide':
    print('You chose divide')
    outcome = first_number / second_number
    print(first_number, ' / ', second_number, ' = ', outcome)
    except ZeroDivisionError:
        print('You cannot divide by zero!')
else:
    print('The option you chose',(calc), 'is not valid!\n Please try this program again. ')