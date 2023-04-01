# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all words in the string
# and print back the most common word in the text.

from collections import Counter
import re

string = 'I wonder if coding nomads are actually more coding or more nomads. Nomads assumes quite an archaic lifestyle which, by definition, is far from coding.'

def getMostFreqWord(string):
    stdString = re.sub('[^\w ]', '', string)
    dictOut = Counter(stdString.lower().split())

    return max(dictOut, key = dictOut.get)


