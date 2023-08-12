# 07. Write a program that generates a random number between 1 and 10 and asks the user to guess it.

import random

random_number = random.randint(1, 10)  # Generate random number between 1 and 10
guess = int(input("Guess the number between 1 to 10 :"))  # Get user's guess

if guess == random_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, the number was", random_number)
