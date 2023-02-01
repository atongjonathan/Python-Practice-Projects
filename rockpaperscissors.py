import random
import time
def play() :
    # getting user input
    
    user = input("Make your choice , 'r' is for Rock 's' is for Scissors and 'p' is for Paper\n")
    computer = random.choice(['r', 'p', 's'])
    print(f"The computer's choice was {computer}")
    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):
        return "You Won!"
    if is_win (computer, user):
       return "You Lost!"


def is_win(player,opponent) :
    # p>r s>p r>s
    if (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's') :
        return True
print(play())

  


