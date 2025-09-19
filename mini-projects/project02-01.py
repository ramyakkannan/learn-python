# number guessing game - tiny quick version & pick range
# https://www.youtube.com/watch?v=8ext9G7xspg - FREECODECAMP
# but the program breaks if you enter anything but a number


import random


def guess(x):
    numtoguess = random.randint(1, x)
    guess = 0
    while guess != numtoguess:

        guess = int(input(f"Guess a number between 1 to {x} : "))

        if guess > numtoguess:
            print("that's too high")

        else:
            print("That's too low")

    print(f"Yay, you guessed the number {numtoguess}!! ⭐")


guess(100)
