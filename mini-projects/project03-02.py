# rock paper sciccors - modular version
# with DRY concept - Don't Repeat Yourself
# https://www.youtube.com/watch?v=yVl_G-F7m8c&t=700s - PROGRAMMING WITH MOSH

import random


ROCK = "r"
PAPER = "p"
SCISSORS = "s"


emojis = {ROCK: "💎", SCISSORS: "✂️", PAPER: "📄"}
choices = tuple(emojis.keys())


def yourchoice():
    while True:
        uchoose = input("Wanna play Rock-Paper-Sciccors? (r/p/s) ").lower()
        if uchoose in choices:
            return uchoose
        else:
            print("Invalid & chose between r/p/s")
            continue


def compchoice(uchoose, cchoose):
    cchoose = random.choice(choices)
    print(f"You chose {emojis[uchoose]} & computer chose {emojis[cchoose]}")


def gamewinner(uchoose, cchoose):
    if uchoose == cchoose:
        print("that's a tie!")

    elif (
        (uchoose == SCISSORS and cchoose == PAPER) or
        (uchoose == ROCK and cchoose == SCISSORS) or
            (uchoose == PAPER and cchoose == ROCK)):
        print("You win ⭐")

    else:
        print("You lose")


def playgame():
    while True:

        yourchoice()

        compchoice(uchoose, cchoose)

        gamewinner(uchoose, cchoose)

        go_on = input("Want to continue? (y/n) ")
        if go_on == "n":
            print("okay bye!")
            break
        elif go_on != ("y" or "n"):
            print("choose again!")
            continue


playgame()
