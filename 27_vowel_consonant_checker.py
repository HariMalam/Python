# Write a program that determines whether a given character is a vowel or consonant.

char = input("Enter a character :").lower()

if char.isalpha() and len(char) == 1:
    if char in "aeiou":
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")
else:
    print("invalid input")
