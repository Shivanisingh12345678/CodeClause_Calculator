def calculate():
    operation = input('''enter the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    number_1 = float(input('enter the first number:'))
    number_2 = float(input('enter the second number:'))
    if operation == '+':
        print('{}+{}='.format(number_1,number_2))
        print(number_1+number_2)
    elif operation == '-':
        print('{}-{}='.format(number_1,number_2))
        print(number_1-number_2)
    elif operation == '*':
        print('{}*{}='.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{}/{}='.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('you entered a wrong math operator!')
    again()

def again():
    calculation_again = input('''
do you want to calculate again 
please type y for yes or N for no
''')
    if calculation_again.upper()=='y':
        calculate()
    elif calculation_again.upper()=='N':
         print('Bye Bye,thank you for coming')
    else:
         again()

calculate()








