# Save allowed user inputs --> check against when user chooses
# Create player inventory --> they can add / remove items
# Players should be able to collect items found in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. 
    # This effects player wins / loses when battling

from random import randint
from random import sample

def gameIntro():
    print("Welcome to this mini Dungeons & Dragons game!!! \nGood Luck in the wars to come! \n")
    name = input('What\'s your name ?')
    print(f"Welcome '{name}'\nMy Game World Intro")
    return print('')

def chooseDoor(nr_doors = randint(2, 8)):
    doors = {str(x): str(x) for x in range(1, nr_doors+1)}
    door = None

    print(f'There are {len(doors)} doors ahead of you. \nWhich way do you go ? \n')

    while door not in doors:
        door = input(f'Select Door Nr. ({[x for x in doors.keys()]}):')

        if door not in doors:
            print(f"You selected '{door}'. Please selected from {doors}")
    return int(door)

def checkRoom():
    lookoptions = {'1': 'Leave','2': 'Look'}
    lookaround = None
    print('You entered an empty room. \nWhat are you gonna do?\n')

    while lookaround not in lookoptions.keys():
        lookaround = input('Look around or Leave (1 = Leave / 2 = Look)?')

        if lookaround not in lookoptions.keys():
            print(f"You selected '{lookaround}'. Please select from {lookoptions}")
    return int(lookaround)

def getPlayerInventory(nr_items = 6):
    possible_items = ['sword', 'shield', 'ring', 'armor', 'amulet', 'boots', 'gloves']
    return {possible_items[x]: 0 for x in range(nr_items)}

# door already chosen; lookaround already chosen
def findRandomItem(inventory):
    emptyitems = [key for key, value in inventory.items() if value == 0]
    randomitem = str(sample(emptyitems, 1)[0])

    print(f"Oh look!! A {randomitem}!!! Do you want to add it to your inventory ? \n")

    takeitem_dict = {'1':'Take item', '2':'Leave item' }
    takeitem = None

    while takeitem not in takeitem_dict.keys():
        takeitem = input(f"Select '1' to take the {randomitem}. Select '2' to leave it \n")

        if takeitem not in takeitem_dict.keys():
            print(f"You selected '{takeitem}'. Please select from {takeitem_dict}")
        elif takeitem == '1':
            inventory[randomitem] += 1
            print(f"{randomitem} has been added to your inventory. \n")
    return inventory

# --- Run Game ----------------------------------------------------------
def fightDragon(inventory):
    fightOptions = {"1": "Fight", "2": "Run"}
    fight = None

    while fight not in fightOptions:
        print('A DRAGON!!! Do you fight it or run for your life ? \n')
        fight = input(f"Do you want to fight the dragon ({fightOptions})  ???")

        if fight not in fightOptions:
            print(f"You selected '{fight}'. Please choose from {fightOptions} \n")

    if fight == '1':
        if inventory['sword'] == 1:
            print("You defeated the dragon. Congratulations!!! \n")
            return 1
        elif 'amulet' in inventory.keys() and inventory['amulet'] == 1:
            print("You couldn't defeat the dragon, but your magic amulet protected you & you're items, though got destroyed in the process \n")
            inventory['amulet'] -= 1
        elif 'shield' in inventory.keys() and inventory['shield'] == 1:
            print("You couldn't defeat the dragon, but you could save yourself thansk to your shield. All your inventory got destroyed though.. \n")
            inventory = {key:0 for key in inventory.keys()}
        else: # lost & died
            print('The dragon devoured you unfortunately :/ You Died & Lost... \n')
            return 0
    return inventory

def playDungAndDrags():
    gameIntro()

    gameFinished = False
    nr_doors = randint(2, 7)
    dragon_door = randint(1, nr_doors)
    playerInventory = getPlayerInventory(nr_items = nr_doors - 1)

    while not gameFinished:
        door = chooseDoor(nr_doors = nr_doors)

        if int(door) != dragon_door:
            check_room = checkRoom()

            if check_room == 2:
                playerInventory = findRandomItem(inventory = playerInventory)
            else:
                continue

        else: # fight dragon...
            dragon_fight = fightDragon(inventory = playerInventory)

            if isinstance(dragon_fight, int):
                gameFinished = True
            else:
                playerInventory = dragon_fight

playDungAndDrags()