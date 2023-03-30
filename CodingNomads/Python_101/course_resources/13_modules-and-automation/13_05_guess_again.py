# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
from random import randint

n_guesses = input('How many guesses do you want to have ?')
nr = int(n_guesses)
tries = nr
num = randint(1, 2 ** nr)
guess = None

while guess != num:
    print(f'You have {tries} tries remaining \n')
    guess = input(f'Guess a number between 1 - {2**nr} :')

    guess = int(guess)

    if guess == num:
        print('Congrats!! You Won!! \n')
    elif guess > num:
        print(f'{guess} is too high\n')
        tries -= 1
    elif guess < num:
        print(f'{guess} is too low \n')
        tries -= 1
    
    if tries == 0:
        print(f'Sorry, you lost. Your Nr was {num}. Better luck next time \n')
        break
    


