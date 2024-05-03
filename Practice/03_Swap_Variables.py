# 03. Write a program that swaps the values of two variables.

a = input("Enter value of a :")
b = input("Enter value of b :")

print("Before swapping a = ", a, " b = ", b)
a, b = b, a  # Swap values using tuple unpacking
print("After swapping a = ", a, " b = ", b)
