# 11. Write a program to calculate the area of a circle using the formula area = pi * radius^2.

import math

radius = float(input("Enter radius of circle :"))

# Calculate the area using the formula
area = math.pi * radius ** 2

# Print the calculated area with 2 decimal
print("Area of Circle is ", f"{area:.2f}")
