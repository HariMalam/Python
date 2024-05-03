# Write a program that generates the pattern:
# *
# **
# ***
# ****
# *****

num = int(input("Enter number :"))

for i in range(1, num + 1):
    print("*" * i)
