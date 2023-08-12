# 19. Write a program that converts a decimal number to binary using recursion.
def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


# Get a decimal number from the user
decimal = int(input("Enter a decimal number :"))

# Call the recursive function to get the binary representation
binary_representation = decimal_to_binary(decimal)

# Print the binary representation
print("Binary representation:", binary_representation)
