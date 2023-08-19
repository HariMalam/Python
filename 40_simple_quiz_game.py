# Create a program that simulates a simple quiz game.

quiz_data = {
    "What is capital of India?": "Delhi",
    "Who is Hacker": "Hari",
    "Which is best country in World": "India",
}

score = 0

for question, answer in quiz_data.items():
    user_answer = input(question + " ").capitalize()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.\nThe correct answer is :", answer)

print("Your final score :", score, "out of", len(quiz_data))
