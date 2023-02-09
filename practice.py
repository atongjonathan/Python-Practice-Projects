from words import words
import random
import string
def get_valid_words(words):
    word = random.choice(words)
    if ' ' in words or '-' in words:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_words(words)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word.upper())
    correctly_guessed = set()


    #getting user input
    
    user_letter = input("Guess a letter: \n").upper()
    used_letters.add(user_letter)
    word_list = [letter if letter in word ] 
    if user_letter in alphabet:
        
        print(f"You have used these letters: "' '.join(used_letters))
        if user_letter in word:
            print("Nice try")
            correctly_guessed.add(user_letter)
            word_letters.remove(user_letter)
        else:
            print("Not quite try again")
    else:
        print(f"Invalid character{user_letter}")


hangman()