import random

def print_separator():
    """Vytiskne oddělovač."""
    print(40 * "-")

def generate_random_number():
    """Generuje náhodné čtyřmístné číslo."""
    number = str(random.randint(1000, 9999))
    while not check_same_numbers(number):
        number = str(random.randint(1000, 9999))
    return number

def check_input_number(guess):
    """Ověření, zda vstupní číslo nezačíná nulou, zda jsou zadány čísla a má délku 4."""
    if guess.startswith("0"):
        print("Your number starts with 0. Enter a 4-digit number, please.")
        return False
    if not guess.isdigit() or len(guess) != 4:
        print("Wrong input, enter a 4-digit number, please.")
        return False
    if len(guess) != len(set(guess)):
        print("Your input contains duplicated numbers, try again.")
        return False
    return True

def check_same_numbers(num):
    """Ověření stejných čísel, aby se neopakovaly."""
    return len(num) == len(set(num))

def pluralize(word, count):
    """Správné zvolení množného či jednotného čísla."""
    if count == 1:
        return word
    else:
        return word + "s"

def play_bulls_and_cows():
    """Zahájení hry Bulls and Cows."""
    print("Hi there!")
    print_separator()
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print_separator()

    number = generate_random_number()
    guesscount = 0

    # Hádání čísla.
    while True:
        guess = input("Enter a number: ")
        guesscount += 1

        if not check_input_number(guess):
            continue

        bulls = 0
        cows = 0
        for i in range(4):
            if guess[i] == number[i]:
                bulls += 1
            elif guess[i] in number:
                cows += 1
        
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {guesscount} guesses.")
            break

        # Správné zvolení jednotného a množného čísla.
        if bulls == 1 and cows == 1:
            print(f"{bulls} bull, {cows} cow")
        elif bulls == 1:
            print(f"{bulls} bull, {cows} cows")
        elif cows == 1:
            print(f"{bulls} bulls, {cows} cow")
        else:
            print(f"{bulls} bulls, {cows} cows")

if __name__ == "__main__":
    play_bulls_and_cows()
