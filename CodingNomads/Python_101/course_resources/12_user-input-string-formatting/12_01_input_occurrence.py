# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
import re
def findFirstLetter(letter = 'o', string = 'hello world'):
    ind = string.find(letter)
    if ind == -1:
        print(f" Letter {letter} not found")
    return ind

chk = findFirstLetter('z', 'kumbaya')