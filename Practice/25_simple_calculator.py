# Write a program that simulates a simple calculator (addition, subtraction, multiplication, division).

num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
operation = input("Enter the operation (+, -, *, /) :")

result = None
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid Operation")

if result is not None:
    print("Result :", result)
