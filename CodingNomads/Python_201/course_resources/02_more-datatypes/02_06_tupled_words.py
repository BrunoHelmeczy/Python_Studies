# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

import re
string = 'I wonder if coding nomads are actually more coding or more nomads. Nomads assumes quite an archaic lifestyle which, by definition, is far from coding.'

def getTupleOfWords(string):
    stdString = re.sub('[^\w ]', '', string.lower())

    return [tuple(wd) for wd in set(stdString.split())]

getTupleOfWords(string)

