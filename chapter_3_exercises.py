#2 write a code segment that prints the number's absolute value without using Python's abs function.

x = int(input('Enter the value for x: '))
if x >= 0:
    print('The absolute value of x is', x )
else:
    print('The absolute value of x is:', x *-1)

#3 Write a loop that counts the number of space characters in a strong

string = input('Enter a string: ')
print(string.count(' '))

#4 assume that variables x and y refer to strings.  Write a code segment that prints these strings in
# alphabetical order. You should assume that they are not equal.

x = input((str('Enter a word for x: ')))
y = input((str('Enter a word for y: ')))

if x > y:
    print(y)
    print(x)
else:
    print(x)
    print(y)

# 5 Explain how to check for an invalid input number and prevent it from being used in a program.

x = int(input('Enter a number: '))

if x >= 0 and x <=100:
    print('We will use this number ')
else:
    print('Rejected!')

#8

x = int(input('Enter a number for x value: '))
y = int(input('Enter a number for y value: '))
oper = str(input("Choose a math operation (+, -, *, /): "))

if oper == "+":
    print(x+y)
elif oper == "-":
    print (x-y)
elif oper == "*":
    print (x*y)
elif oper =="/":
    print(x/y)
else:
    print('well thats strange')

#9

