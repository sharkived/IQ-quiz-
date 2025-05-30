import time
import colorama
from colorama import Fore, Style, init

print(Fore.CYAN + "Welcome to my IQ Test Quiz.")
print(Fore.CYAN + f"Please answer the following questions and learn your IQ based on your answers!")

score = 0

#questions

questions = [
    {
        "question": "1. What comes next in the series: 2, 4, 8, 16, ?",
        "options": ["A. 18", "B. 20", "C. 24", "D. 32",],
        "answer": "D"
    },

    {
        "question": "2. Which one is the odd one out?\nCat, Dog, Rabbit, Carrot",
        "options": ["A. Cat", "B. Dog", "C. Rabbit", "D. Carrot"],
        "answer": "D"
    },

    {
        "question": "3. If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. Cannot Say"],
        "answer": "A"
    },

    {
        "question": "4. Which number is missing: 1, 4, 9, 16, ?, 36",
        "options": ["A. 20", "B. 25", "C. 30", "D. 32"],
        "answer": "B"
    },

    {
        "question": "5. If you rearrange the letters 'CIFAIPC', you get the name of a:",
        "options": ["A. Country", "B. City", "C. Ocean", "D. Animal"],
        "answer": "B" #PACIFIC
    }
]

time.sleep(1)

#ask each question

for q in questions:
    print(Fore.WHITE + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input(Fore.YELLOW + "Your Answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print(Fore.GREEN + "Correct!!\n")
        score += 1
    else:
        print(Fore.RED + f"Wrong answer! The correct answer is {q['answer']}.\n")

    time.sleep(1)

# Final score
print(Fore.YELLOW + f"🎯 Your final score: {score} out of {len(questions)}")
if score == 5:
    print("Genius! 🧠✨")
elif score >= 3:
    print(Fore.CYAN + "Nice work! You’ve got potential. 🌟")
else:
    print(Fore.MAGENTA + "Keep practicing! 💪")
