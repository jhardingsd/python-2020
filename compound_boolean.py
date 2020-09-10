number = int(input('Enter the numeric grade: '))
if number > 100:
    print('Error.  Number must be between 0 and 100')
elif number < 0:
    print('Error.  Number must be between 0 and 100')
else:
    print('')

print(number)

number2 = int(input('Enter the numeric grade: '))
if number2 > 100 or number2 < 0:
    print('ERROR!!!!!')
else:
    print(number2)

number3 = int(input('Enter the numeric grade: '))
if number3 >=0 and number3 <=100:
    print(number3)
else:
    print('Error!!!')
