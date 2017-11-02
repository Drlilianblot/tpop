import random

# these Constants are defined to facilitate code reading
CAR = 'CAR'
GOAT = 'GOAT'
STICK = 'STICK'
CHANGE = 'CHANGE'

def setGame():
    '''
    Set the game hiding a car behind one of the three doors, 
    and hiding a goat behind the two remaining doors.
    
    @return: 
    a list of size three, containing two gameshow.GOAT and 
    one gameshow.CAR at random position.
    '''
    doors = [GOAT] * 3    
    car = random.randint(0,2)
    doors[car] = CAR
    return doors

def changeChoice(initialChoice, shownDoor, doors):
    '''
    Return the prize (GOAT or CAR) behind the door when 
    the player changed his/her initial choice.
    
    @param initialChoice: an int representing the position of 
    the door the player chose initially.
    
    @param shownDoor: an int representing The position of the 
    door shown to the player after he/she made his/her initial 
    choice.
    
    @param doors: a list of size 3 representing the current 
    set up of the game, e.g. the object hidden behind each door.
    
    @return: the object hidden behind the corresponding door,
    after the player changed his/her choice. the value return is 
    either gameshow.GOAT or gameshow.CAR.
    '''
    indices = list(range(len(doors)))
    indices.remove(initialChoice)
    indices.remove(shownDoor)
    return doors[indices[0]]

def stickToChoice(initialChoice, doors):
    '''
    returns the object hidden behind the player's initial choice.
    
    @param initialChoice: an int representing the position of the 
    initial door chosen by the player
    
    @param doors: a list of size 3 representing the current 
    set up of the game, e.g. the object hidden behind each door.
   
    @return: the object hidden behind the corresponding door,
    after the player changed his/her choice. the value return is 
    either gameshow.GOAT or gameshow.CAR.
    '''
    return doors[initialChoice]

def showDoor(initialChoice, doors):
    for i in range(len(doors)):
        if(i != initialChoice and doors[i] == GOAT):
            return i
    raise ValueError('Unexpected Game State')

def game(stick = 0):
    doors = setGame()
    choice = random.randint(0,2)
    show = showDoor(choice, doors)
##    stick = random.randint(0,1)
    if stick == 0: # player change his/her choice
        return CHANGE, changeChoice(choice, show, doors)
    else:
        return STICK, stickToChoice(choice, doors)

def simulation(sampleSize):
    table = [[0,0],[0,0]]
    for i in range(sampleSize):
        strategy, win = game(1)
        if(strategy == STICK):
            if(win == CAR):
                table[0][0] += 1
            else:
                table[0][1] += 1
        else:
            if(win == CAR):
                table[1][0] += 1
            else:
                table[1][1] += 1

    print(table)

simulation(10000)
            
    
    
