# Write a Python program that takes a string as input and counts the occurrences of each character.
# Print the character along with its count.

string = input("Enter string :")

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\ncharacter count")
for char, count in char_count.items():
    print(f"'{char}' : {count}")
