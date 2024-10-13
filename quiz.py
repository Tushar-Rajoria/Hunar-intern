questions = ["What is the capital of India?","Which planet is known as the Red Planet?","Who is Prime Minister of India?",]
answers = ["Delhi", "Mars", "Narendra Modi"]
score = 0
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")

    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", answers[i])

print("\nYour final score is:", score, "out of", len(questions))
