# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:
import random as rn

min = 1
max = 10

guess = None
num = rn.randint(min, max)
prompt = str('Guess a Number between ' + str(min) + ' & ' + str(max))
while guess != num:
    guess = input(print(prompt))

    if int(guess) == num:
        print('Congrats, you won! The answer was ' + str(num))
        break
    elif int(guess) > num:
        print('Your guess is too high')
    elif int(guess) < num:
        print('Your guess is too low')