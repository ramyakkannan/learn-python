# rock paper sciccors - amature version
# https://www.youtube.com/watch?v=yVl_G-F7m8c&t=700s - PROGRAMMING WITH MOSH

import random


choices = ("r", "p", "s")  # as a tuple so uneditable
emojis = {"r": "💎", "s": "✂️", "p": "📄"}

while True:

    uchoose = input("Wanna play Rock-Paper-Sciccors? (r/p/s) ").lower()
    if uchoose not in choices:
        print("Invalid & chose between r/p/s")
        continue

    # continue here or else the program crashes

    cchoose = random.choice(choices)

    print(f"You chose {emojis[uchoose]} & computer chose {emojis[cchoose]}")

    if uchoose == cchoose:
        print("that's a tie!")

    elif (
        (uchoose == "s" and cchoose == "p") or
        (uchoose == "r" and cchoose == "s") or
            (uchoose == "p" and cchoose == "r")):
        print("You win ⭐")

    else:
        print("You lose")

    go_on = input("Want to continue? (y/n) ")
    if go_on == "n":
        print("okay bye!")
        break
    elif go_on != ("y" or "n"):
        print("choose again!")

# FUTURE DEV IDEAS
# keep score
# get user name and replace "You" with it
# make it two player with boo?
