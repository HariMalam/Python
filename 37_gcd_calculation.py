# Write a program that calculates the GCD (greatest common divisor) of two numbers using the Euclidean algorithm.

num1 = int(input("Enter First Nuber :"))
num2 = int(input("Enter Second Nuber :"))

# Euclidean algorithm
while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD:", num1)
