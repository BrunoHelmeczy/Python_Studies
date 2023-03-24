import random as rn

def check_input(input):
    try:
        val = int(input)
        return True
    except ValueError:
        print('value is not integer')
        return False

num = rn.randint(1, 10)
guess = None

while guess != num:
    guess = input("Guess a nr between 1 & 10: ")

    if not check_input(guess):
        print('You should input an Integer Nr')
        continue

    if int(guess) == num:
        print('congratulations! you won')
        break
    elif int(guess) > num:
        print('nope, sorry, too high')
    elif int(guess) < num:
        print('nope, sorry, too low')

# from bash: call py CodingNomads/Python_101/exercises/guess.py