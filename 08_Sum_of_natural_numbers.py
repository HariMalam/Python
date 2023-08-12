# 08. Create a program that calculates the sum of the first n natural numbers.

num = int(input("Enter Positive Number :"))  # Get number from user
sum_numbers = int((num * (num + 1)) / 2)  # Sum formula for first n natural numbers
print("Sum of first", num, "natural numbers:", sum_numbers)
