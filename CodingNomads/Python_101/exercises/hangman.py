import urllib.request as req
import random
from itertools import compress

def getHangmanWord():
    word_site = 'https://www.mit.edu/~ecprice/wordlist.10000'

    Words = req.urlopen(word_site).read().decode('utf-8').replace('\n', ' ').split(' ')
    MyWords = list(compress(Words, [len(word) >= 5 for word in Words]))

    return MyWords[random.randint(0, len(MyWords) - 1)]

word = getHangmanWord()
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
        print(f'Your word to guess was {word}')
        break

