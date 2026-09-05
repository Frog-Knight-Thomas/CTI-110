# Michael Baker
# 9/2/26 
# P2Lab1
# using the radius provided by user, program will calculate details of the circle

import math

radius = float(input("What is the radius of the circle? "))
diameter = radius * 2
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print("The diameter of the circle is", diameter)
print("The circumference of the circle is", circumference)
print("The area of the circle is", area)
