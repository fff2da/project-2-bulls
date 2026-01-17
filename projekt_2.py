"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""

import random

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")

numbers = list("0123456789")
random.shuffle(numbers)

if numbers[0] == "0":
    numbers[0], numbers[1] = numbers[1], numbers[0]

secret_number = "".join(numbers[:4])
guesses = 0

while True:
    guess = input("Enter a number: ")

    if not guess.isdigit():
        print("Please enter only numbers.")
        continue

    if len(guess) != 4:
        print("Number must have 4 digits.")
        continue

    if guess[0] == "0":
        print("Number cannot start with 0.")
        continue

    if len(set(guess)) != 4:
        print("Digits must be unique.")
        continue

    guesses += 1

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    
    if bulls == 4:
        print("-----------------------------------------------")
        print("Correct, you've guessed the right number")
        print(f"in {guesses} guesses!")
        print("-----------------------------------------------")
        break
    else:
        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_text}, {cows} {cow_text}")
        print("-----------------------------------------------")
