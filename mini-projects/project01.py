# dice rolling game
# https://www.youtube.com/watch?v=yVl_G-F7m8c&t=700s - PROGRAMMING WITH MOSH


import random as randd
count = 0
sum = 0
# put the count & sum above the loop to keep it from refreshing!


while True:

    roll = input("Roll the dice? (y/n) ").lower()
    if sum >= 30:
        print(f"So far you played {count} times, and your sum is {sum}")
        print("And you've reached maximum moves for now!🙊 See you later! 😊")
        break
    elif roll == "y":
        die1 = randd.randint(1, 6)
        die2 = randd.randint(1, 6)
        count += 1
        sum += die1 + die2
        print(f"You rolled a {die1} and a {die2}!")
        print(f"So far you played {count} times, and your sum is {sum}")
    elif roll == "n":
        print("Thanks for playing! 😊")
        print(f"So far you played {count} times, and your sum is {sum}")
        break
    else:
        print("Invalid choice, wanna try again? 😲")
        print(f"You've already played {count} times!")

# couldn't do an 'and' operator with roll == n because it comes after roll == y
# FUTURE DEV IDEAS
