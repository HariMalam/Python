# Create a program that simulates a rock-paper-scissors game.

player1 = input("Player 1, choose rock, paper, or scissors: ").lower()
player2 = input("Player 2, choose rock, paper, or scissors: ").lower()

# Determine the winner
if player1 == player2:
    result = "It's a tie!"
elif player1 == "rock":
    if player2 == "scissors":
        result = "Player 1 wins!"
    else:
        result = "Player 2 wins!"
elif player1 == "paper":
    if player2 == "rock":
        result = "Player 1 wins!"
    else:
        result = "Player 2 wins!"
elif player1 == "scissors":
    if player2 == "paper":
        result = "Player 1 wins!"
    else:
        result = "Player 2 wins!"
else:
    result = "Invalid input."

print(result)
