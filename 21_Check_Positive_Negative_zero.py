# Write a program that checks if a given number is positive, negative, or zero.

num = int(input("Enter a number :"))
if num > 0:
    print(num, "is positive number")
elif num < 0:
    print(num, "is negative number")
else:
    print(num, "is zero")
