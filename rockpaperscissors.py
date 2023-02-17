import random
import time
def play(user,computer) :
    # getting user input
    
    # user = input("Make your choice , 'r' is for Rock 's' is for Scissors and 'p' is for Paper\n")
    # computer = random.choice(['rock', 'paper', 'scissors'])
    if user == computer:
        print(f"What a coincidemce the computer's choice was also{computer}")
        return 'It\'s a tie'
    if is_win(user, computer):
        print(f"Fortunately the  computer's choice was {computer}")
        return "You Won!"
    if is_win (computer, user):
        print(f"Unfortunately the computer's choice was {computer}")
        return "You Lost!"


def is_win(player,opponent) :
    # p>r s>p r>s
    if (player == 'paper' and opponent == 'rock') or (player == 'scissors' and opponent == 'paper') or (player == 'rock' and opponent == 'scissors') :
        return True
print(play('rock','paper'))

  


