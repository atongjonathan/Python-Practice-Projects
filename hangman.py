import random
import string
from words import words



def get_valid_word(word):
    word = random.choice(words).upper()
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    valid_used_letters = used_letters

    # getting user input
    while len(word_letters) > 0:
        print("You have used these letters: \n", ' '.join(valid_used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word", ' '.join(word_list))
        user_letter = input("Guess the letter: \n").upper()
        while user_letter not in alphabet:
            used_letters.remove(valid_used_letters)
            print("Invalid Character")
            break
        while user_letter in used_letters:
            print("You literally just guessed that letter. Please try again")
            break
        if alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word:
                word_letters.remove(user_letter)


        else:
            print("Invalid character")
    print(f"You have guessed the word {word}! correctly!")


hangman()





