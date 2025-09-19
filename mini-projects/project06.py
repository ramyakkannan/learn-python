# hangman game - using CHATGPT HELP
# https://www.youtube.com/watch?v=8ext9G7xspg - FREECODECAMP
# https://chatgpt.com/share/68cb7cad-b168-800a-a979-ea643bd16cdb - CHATGPT chat


# NEW LEARNINGS - list with strings, pop, enumerate, import python file


import random
from wordlist import words


def valid_word(words):
    game_word = random.choice(words)
    while " " in game_word or "-" in game_word:
        if len(game_word) >= 7:
            game_word = random.choice(words)
            continue
    return game_word


game_word = valid_word(words).upper()


# all game variables

game_word_set = set(game_word)
display_word = ["_" for letter in game_word]
game_word_length = len(game_word)
gamemode = "short one" if game_word_length <= 5 else "long one"
all_guesses = []
lives = [" ⭐  ", " ⭐  ", " ⭐  ", " ⭐  ", " ⭐  ", " ⭐  ", " ⭐  "]
# alt_lives = game_word_length + 2


# # welcome message

print("welcome to the hangman game!")
print(
    f"guess the word is a {gamemode} with {game_word_length} letters : {display_word}")
print(f"you have {lives} : 7 lives")

# # game logic

while len(game_word_set) != 0:

    u_guess = input("guess an alphabet: ").upper()

    if lives == []:
        print(f"You ran out of 💔 lives! the word was '{game_word}' ")
        break

    if len(u_guess) != 1 or not u_guess.isalpha() or u_guess in all_guesses:
        print("try again")
        continue
    else:
        all_guesses.append(u_guess)

    if u_guess in game_word_set:
        game_word_set.remove(u_guess)

        for x, letter in enumerate(game_word):
            if letter == u_guess:
                display_word[x] = u_guess
        print("\ngood guess 🟢")

    else:
        print("\nbad guess 🔴")
        lives.pop()

    print("word is     : ", " ".join(display_word))
    print(f"you guessed {all_guesses} and {lives} left")
print(f"Yay, you guessed the word {game_word} ✨")


# FUTURE DEV IDEAS
# length of word = number of lives
# hangman figure draw as game goes on?
# keep score of all games - continue playing loop?
