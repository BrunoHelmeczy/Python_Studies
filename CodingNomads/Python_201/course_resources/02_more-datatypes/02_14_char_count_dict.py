# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
from collections import Counter

string = 'This is meant to be a veeeery long string to be extracted and organized using Counter'

chk = dict(Counter(string.replace(' ', '').lower()))

dict(sorted(chk.items(), key = lambda item: item[0]))

def getLetterFrequency(string, sort=True):
    LetterCount = dict(Counter(string.replace(' ', '').lower()))

    if sort == True:
        return dict(sorted(LetterCount.items(), key = lambda item: item[0]))
    else:
        return LetterCount

getLetterFrequency(string)
getLetterFrequency(string, sort = False)
