# Create a program that calculates the sum of all even numbers between 1 and n.

num = int(input("Enter number :"))

sum_even = 0
for i in range(1, num):
    if i % 2 == 0:
        sum_even += i
print("sum of even numbers :", sum_even)
