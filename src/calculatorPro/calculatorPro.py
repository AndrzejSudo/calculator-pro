
print('Welcome to calculator')
print('''Available operation commands:
'+' for addition
'-' for subtraction
'*' for multiplication
'/' for division''')

cmd = ''

while cmd != 'n' and cmd != 'N':

    try: # this can also be verified with if statement and .isdigit() method.
        x = int(input('Enter 1st digit: '))
        z = input('Choose operation: ')
        y = int(input('Enter 2nd digit: '))

    except ValueError:
        print('\nInvalid number, try again\n')
        continue
    else:
        if z == '+':
            add = f'{x} + {y} = {x+y}'
            print(add)
        elif z == '-':
            sub = f'{x} - {y} = {x-y}'
            print(sub)
        elif z == '*':
            mul = f'{x} * {y} = {x*y}'
            print(mul)
        elif z == '/':
            div = f'{x} / {y} = {x/y}'
            print(div)
        else:
            print(f'''\n{'Invalid operation'.center(25, '*')}
Available operations are:
'+' for addition
'-' for subtraction
'*' for multiplication
'/' for division\n''')
            continue

    while True:
        cmd = input('Do you want to continue? [Y/N]: ')
        if cmd == 'N' or cmd == 'n':
            break
        elif cmd == 'Y' or cmd == 'y':
            break
        else:
            print('\nNot recognized input, type "Y" for "yes" or "N" for "no".\n')

print('\nAlright, have a nice day\n')
