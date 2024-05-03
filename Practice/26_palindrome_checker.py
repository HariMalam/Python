# write a Python program to check if a given word is a palindrome or not.

word = input("Enter a word :")

word = word.lower()

reversed_word = word[::-1]

if word == reversed_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
