# 1st tasks:
# 1) Ask player name
# 2) Display greeting message + game world intro
# 3) Present choice of 2 doors
    # left:     empty room
    # right:    encounter dragon
# 4) both cases: option to return to previous room or interact further
# 5) empty room --> 
    # leave
    # look around --> find sword. 
        # take it 
        # leave it
# 6) encounter dragon 
    # fight it
        # have sword from other room --> then they will be able to defeat it and win the game.
        # don't have sword, then they will be eaten by the dragon and lose the game.
    # leave

print("Welcome to this mini Dungeons & Dragons game!!! \n Good Luck in the wars to come! \n")

name = input('What\'s your name ?')

print('Welcome ' + name + '\n My Game World Intro' + '\n')

def chooseDoor():
    print('There are 2 doors ahead of you. \nWhich way do you go ? \n')
    door = input('Select Left/Right (L/R):')
    return door

def checkEmptyRoom():
    print('You went left & entered an empty room. \nWhat are you gonna do?\n')
    lookaround = input('Look around or Leave (Leave = "Leave" / Look = anything else)?')
    return lookaround
    
def findSword():
    print('Wow! The sword of excalibur! Do you want to take it or leave it ?')
    getsword = input('Do you want to pick up the sword ? (y/n)')
    return getsword

def fightDragon():
    print('daaaaaamn, a dragon... what are you gonna do ?\n')
    fightdragon = input('Fight the Dragon, or Run ? (y/n)')
    return fightdragon


gameFinished = False
sword = None
door = chooseDoor()

while not gameFinished:
    if door.lower() == 'l':
        lookaround = checkEmptyRoom()
        if lookaround == 'Leave':
            print('You\'re back in the main hall now...\n')
            door = chooseDoor()
            continue
        else:
            sword = findSword()
            door = chooseDoor()
            continue
    elif door.lower() == 'r':
        fightdragon = fightDragon()

        if fightdragon == 'n':
            door = chooseDoor()
            continue
        else:
            if sword in [None, 'n']:
                print("You dummy... how are you gonna fight without a weapon ? You're dead & lost")
            elif sword == 'y':
                print("You amazing bastard.. You killed the dragon & won & acquired bragging rights")

        gameFinished = True
        continue



