import sys

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("After each guess, tell me if your number is (h)igher, (l)ower, or (c)orrect.")
    
    low = 1
    high = 100
    attempts = 0
    
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is {guess}.")
        hint = input("Is your number higher (h), lower (l), or correct (c)? ").strip().lower()
        
        if hint == 'c':
            print(f"I've guessed your number {guess} in {attempts} attempts!")
            break
        elif hint == 'h':
            low = guess + 1
        elif hint == 'l':
            high = guess - 1
        else:
            print("Please enter 'h', 'l', or 'c'.")
    else:
        print("It seems there is a mistake! Did you change your number?")

if __name__ == "__main__":
    number_guessing_game()
