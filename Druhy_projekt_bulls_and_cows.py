"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Bulls & Cows
author: Veronika Oburkova
email: oburkova.veronika@gmail.com
discord: veronika.007
"""

import random
odd = 40 * "-"

def check_same_numbers(num):
    return len(num) == len(set(num))
"""Kontrola stejnych cisel, aby se neopakovaly."""

print("Hi there!")
print(odd)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(odd)
print(odd)
number = str(random.randint(1000, 9999))

while not check_same_numbers(number):
    number = str(random.randint(1000, 9999))

guesscount = 0
while True:
    guess = input("Enter a number: ")
    guesscount += 1
    if not guess.isnumeric() or len(guess) != 4:
        print("Wrong input, try again.")
        print(odd)
        continue
    if not check_same_numbers(guess):
        print("Your input contains duplicated numbers, try again.")
        continue

    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1
    print(str(bulls)+" bulls, "+str(cows)+" cows")
    if bulls == 4:
        print("Correct, you've guessed the right number in", guesscount, "guesses.")
        break
