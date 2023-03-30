# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

from random import randint

nr = randint(0, 1000000000)
guess = None

while nr != guess:
    guess = input('Guess a Nr between 0 - 1,000,000,000\n')
    guess = int(guess)

    if guess == nr:
        print('Yaaay!!! You\'re awesome. You won\n')
    elif guess > nr:
        print(f'You guessed {guess} & that\'s too high. keep going \n')
    else:
        print(f"You guessed {guess} & that\'s too low. Keep trying \n")

