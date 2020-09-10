import math

area = float(input('Enter the area: '))
if area > 0:
    radius = (area / math.pi)
    print('The radius is:', radius)
else:
    print('Error: the area must be a positive number.')

first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))

if first > second:
    maximum = first
    minimum = second
else:
    maximum = second
    minimum = first

print('Maximum: ', maximum)
print('Minimum:', minimum)

# if <condition>:
#    <sequence of statements-1>
# else
#   <sequence of statements-2>
# python includes functions that make that laste statement unncessary

first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
print('Maximum:', max(first,second))
print('Minimum:', min(first,second))


# Multiway statement example

if number > 89:
    letter = 'A'
elif number >79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'
print('The letter grade is', letter)


