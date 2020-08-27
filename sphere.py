import math
math.pi
pi = math.pi
radius = float(input("Enter radius:  "))
diameter = radius*2
circumference = diameter*pi
surface_area = 4*pi*radius**2
volume = (4/3)*pi*radius**3

print("Diameter: ",diameter)
print("Circumference: ",circumference)
print("Surface area: ", surface_area)
print("Volume: ",volume)