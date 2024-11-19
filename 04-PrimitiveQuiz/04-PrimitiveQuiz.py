# A quiz where it uses list and loops to see how many are correct answer

# List of questions about capitals of many european countries
questions = [
    "What is the capital of Germany?",
    "What is the capital of France?",
    "What is the capital of Italy?",
    "What is the capital of Spain?",
    "What is the capital of Turkey?",
    "What is the capital of Poland?",
    "What is the capital of Norway?",
    "What is the capital of Netherlands?",
    "What is the capital of Austria?",
    "What is the capital of Switzerland?"
    ]
# Answers correlating to questions
answers = ["Berlin", "Paris", "Rome", "Madrid", "Ankara",
    "Warsaw", "Oslo", "Amsterdam", "Vienna", "Bern"]

# Initialize score counter
score = 0

for i in range(len(questions)):
    print(questions[i]) # Display current question

    # Gets answer and convert it to lowercase for case sensitive comparison
    answer = input("Enter your Answer: ").strip()
    answer = answer.capitalize()

    # Check if answer match the correct answer
    if answer == answers[i]:
        print("Excellent! Your answer is Correct")
        score = score + 1 # Increase the score by 1 for each correct answer
    else:
        print("Try again, the answer is:", answers[i]) # Provide correct answer if wrong

print(f"\033[1mYour score is {score}/10\033[0m") # Show total score