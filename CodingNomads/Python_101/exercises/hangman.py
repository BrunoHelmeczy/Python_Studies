# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

# TODO:s
    # DONE: limit inputs to alphanumeric + single character
    # DONE: use counter for wrong tries remaining
    # generate words randomly

word = 'coding nomads'
guesses = ''
toshow = ''.join([w if w in guesses or w == ' ' else '_' for w in word])
lives = 5

print('Welcome to this hangman game.\n')

while (toshow.find('_') != -1):
    print(' Here is your word to guess: '
     f"{toshow}")
    print(f"Lives remaining: {lives} \n")

    guess = input('Guess a letter: ')

    if guess in guesses: # wrote a letter again
        print(f'You guessed \'{guess}\' before already. Try again \n')
        continue
    elif (len(guess) > 1) or (guess.isalpha() == False):
        print('Limit your guesses to alphabetic characters only \n')
        continue

    guesses += guess

    if (guess in word):
        print(f'Congrats!! \'{guess}\' was a good guess. Keep it going \n')
    else:
        print(f'Sorry!! \'{guess}\' was a bad guess. Keep trying \n')
        lives -= 1


    print(f'Your letters guessed until now: {set([w for w in guesses])} \n')
    toshow = ''.join([w if w in guesses or w == ' ' else '_' for w in word])

    if (toshow.find('_') == -1):
        print(f'Congrats!!! You won!!! \nYour word was \'{word}\'')
    elif lives == 0:
        print('You Lost. Better luck next time \n')
        break








