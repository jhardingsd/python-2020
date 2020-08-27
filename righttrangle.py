import math

a= float(input("Enter the first side: "))
b= float(input("Enter the second side: "))
c= float(input("Enter the third side: "))


if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
