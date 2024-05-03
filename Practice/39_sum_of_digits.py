# Write a program that calculates the sum of digits of a given number.

num = int(input("Enter number :"))

str_num = str(num)
sum_of_digit = 0
for digit in str_num:
    digit = int(digit)
    sum_of_digit += digit

print("sum of all digits are ", sum_of_digit)
