import random

def guess(x):
    random_number = random.randint(1,x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input(f"guess a number between 1 and {x}: "))
        if user_guess < random_number:
            print("sorry, guess again. too low")
        elif user_guess > random_number:
            print("sorry guess again. too high")
    print(f"woow you guessed the correct number {user_guess}")

guess(10)
