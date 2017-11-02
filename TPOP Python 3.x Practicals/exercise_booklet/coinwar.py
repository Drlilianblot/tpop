import random

# these Constants are defined to facilitate code reading
COIN_HEAD = 'HEAD'  # represent the head of a coin
COIN_TAIL = 'TAIL'  # represent the tail of a coin

def flipCoin():
    '''
    flip a coin randomly and return one of the two faces of a 
    coin (e.g. COIN_HEAD, or COIN_TAIL).
    '''
    flip = random.randint(0, 1)
    if (flip == 0):
        return COIN_HEAD
    else:
        return COIN_TAIL
    
def coinwar(coins, maxIter):
    '''
    Run a single game of the coin war. The game terminates when on
    of the player as no more coins or when we have reach maxIter 
    rounds without a winner. The game is a draw if no winner is 
    found after maxIter rounds have been done.
    
    @param coins: the initial number of coins for each player.
    @param maxIter: the maximum number of rounds before the game 
    is declared a draw
    @return:  
    0 if it is a draw after maxIter iteration,
    1 if DIFF wins,
    2 if SAME wins.
    '''
    same = diff = coins
    rounds = 0
    while same > 0 and diff > 0 and rounds < maxIter:
        sameFlip = flipCoin()
        diffFlip = flipCoin()
        if(sameFlip == diffFlip):
            same += 1
            diff -= 1
        else:
            same -= 1
            diff += 1

        rounds += 1

    if same == 0:
        return 2
    elif diff == 0:
        return 1
    else:
        return 0


def main():
    '''
    runs a simulation of 10,000 games and display the result.
    '''
    sameWins = diffWins = draws = 0
    for rounds in range(10000):
        gameResult = coinwar(20, 1000)
        if gameResult == 0:
            draws += 1
        elif gameResult == 1:
            diffWins += 1
        elif gameResult == 2:
            sameWins += 1

    print("diff =%d, same = %d, draws = %d" % (diffWins, sameWins, draws))

main()
