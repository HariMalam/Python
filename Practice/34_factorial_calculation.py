# Create a program that calculates the factorial of a given number using a loop.

num = int(input("Enter number :"))

fact = 1
for i in range(1, num+1):
    fact *= i

print(f"Factorial of {num} is {fact}")
