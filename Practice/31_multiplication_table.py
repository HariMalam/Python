# Write a program that prints the multiplication table of a given number.

num = int(input("Enter number :"))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)
