import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the words list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6 # trial numbers

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # print used letter
        print("you have ", lives, "lives left and you have used these letter: ", " ".join(used_letters))

        # what's the current world is (ie: w - rd)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: ", " ".join(word_list))

        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # take away a life if the choice is wrong
                print("letter is not in the word. ")
        elif user_letter in used_letters:
            print("you have already used that character. please try again.")

        else:
            print("invalid character. please try again")

    # gets here when len(word_letter) == 0 or lives == 0
    if lives == 0:
        print("you died, sorry. the word was", word)
    else:
        print("you have guessed the word", word, "!!")


hangman()
