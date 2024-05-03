# 15. Write a program that converts a given integer into its binary representation.

decimal = int(input("Enter the decimal number : "))

# Convert to binary using built-in bin() function
binary = bin(decimal)[2:]  # [2:] to remove the '0b' prefix

print("Binary representation    :", binary)
