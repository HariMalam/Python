# 20. Create a program that calculates the factorial of a given number using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number :"))

# Call the recursive function to calculate the factorial
fact = factorial(num)

print("factorial of", num, "is", fact)
