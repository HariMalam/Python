# 10. Create a program that generates the Fibonacci sequence up to a specified number of terms.

# Function to generate the Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]  # List to store the sequence
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)  # Append the next_num to the list
    return fib_sequence


terms = int(input("Enter the number of terms for Fibonacci sequence :"))
fibonacci_sequence = fibonacci(terms)  # Call the fibonacci function to get the sequence
print("Fibonacci sequence :", fibonacci_sequence)
