import random
def play():
    #p>r r>s s>p
    computer = random.choice(['r', 'p', 'c'])
    user = ""

    user = input("Choose your choice 'r' for rock, 'p' for paper, or 's' for scissors\n").lower()
    print(f"The computer's choice was {computer}")


    if user == computer:
        return 'It\'s a tie'
    if iswin(user, computer):
        return 'You Won!'
    return 'You lost'
    
    


def iswin(user, computer):
    if(user == 'p' and computer == 'r') or (user == 'r' and computer == 's') or (user == 's' and computer == 'p'):
        return True
print(play())
