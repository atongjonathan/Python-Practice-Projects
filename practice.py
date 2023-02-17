
def accum(player1, player2):
    # p>r r>s s>p
    if player1 == player2 :
        return "Draw"
    if is_win(player1,player2):
        return "Player 1 won "
    if is_win(player2,player1):
        return "Player 2 won " 

def is_win(player,opponent) :
    # p>r s>p r>s
    if (player == 'paper' and opponent == 'rock') or (player == 'scissors' and opponent == 'paper') or (player == 'rock' and opponent == 'scissors') :
        return True
print(accum('rock','rock'))


