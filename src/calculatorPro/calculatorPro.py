import sys

print('Welcome to calculator pro')

class Calculator():
    operators = ['+', '-', 'x', '/', '^']

    def __init__(self) -> None:
        while True:
            print('Enter 1st number')
            try:
                self.num1 = float(input('> '))
            except ValueError:
                print('Invalid number')
                continue
            break
        print(self.num1)

        while True:
            print('Select operator')
            for o in Calculator.operators:
                print(o, end=' | ')
            print('')
            self.operator = input('> ')
            if self.operator in Calculator.operators:
                break
            else:
                print('Invalid operator')
                continue
        print(self.num1, ' ', self.operator)

        while True:
            print('Enter 2nd number')
            try:
                self.num2 = float(input('> '))
            except ValueError:
                print('Invalid number')
                continue
            break
        print(self.num1, ' ', self.operator, ' ', self.num2, ' = ', end='')
        
        if

Calculator()

# print('Welcome to calculator')
# print('''Available operation commands:
# '+' for addition
# '-' for subtraction
# '*' for multiplication
# '/' for division''')

# cmd = ''

# while cmd != 'n' and cmd != 'N':

#     try: # this can also be verified with if statement and .isdigit() method.
#         x = int(input('Enter 1st digit: '))
#         z = input('Choose operation: ')
#         y = int(input('Enter 2nd digit: '))

#     except ValueError:
#         print('\nInvalid number, try again\n')
#         continue
#     else:
#         if z == '+':
#             add = f'{x} + {y} = {x+y}'
#             print(add)
#         elif z == '-':
#             sub = f'{x} - {y} = {x-y}'
#             print(sub)
#         elif z == '*':
#             mul = f'{x} * {y} = {x*y}'
#             print(mul)
#         elif z == '/':
#             div = f'{x} / {y} = {x/y}'
#             print(div)
#         else:
#             print(f'''\n{'Invalid operation'.center(25, '*')}
# Available operations are:
# '+' for addition
# '-' for subtraction
# '*' for multiplication
# '/' for division\n''')
#             continue

#     while True:
#         cmd = input('Do you want to continue? [Y/N]: ')
#         if cmd == 'N' or cmd == 'n':
#             break
#         elif cmd == 'Y' or cmd == 'y':
#             break
#         else:
#             print('\nNot recognized input, type "Y" for "yes" or "N" for "no".\n')

# print('\nAlright, have a nice day\n')
