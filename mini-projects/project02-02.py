# number guessing game - stable
# https://www.youtube.com/watch?v=yVl_G-F7m8c&t=700s - PROGRAMMING WITH MOSH

import random

guesscount = 0
randomguessingnumber = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        guesscount += 1

        if guesscount > 10:
            print("You guessed more than 10 times, loser!😂")
            break

        elif guess > randomguessingnumber:
            print("Too high!")
            print(f"You guessed {guesscount} times!")

        elif guess < randomguessingnumber:
            print("Too low!")
            print(f"You guessed {guesscount} times!")

        else:
            print("Congratulations! You guessed the number! ⭐")
            print(f"It took you {guesscount} times to find it!")
            break

    except ValueError:
        print("Be serious & enter a valid number!")


# FUTURE DEV IDEAS
# nearer the number = better hint "getting closer" ?
