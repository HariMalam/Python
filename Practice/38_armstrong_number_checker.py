# Write a Python program to check if a given number is an Armstrong number.
# An Armstrong number is one where the sum of its digits,
# each raised to the power of the number of digits, is equal to the number itself.

num = int(input("Enter number :"))

num_str = str(num)
num_digit = len(num_str)

sum_of_digits = sum(int(digit) ** num_digit for digit in num_str)

if num == sum_of_digits:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")