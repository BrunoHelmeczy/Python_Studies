# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from random import randint
# Write your code below here

def genRandList(nrs = 25):
    return [randint(-100, 100) for x in range(nrs)]

def genTuplesFromList(nrList = genRandList(), tupleLength = 2):
    nrList.sort()

    out = [tuple(nrList[i:(i + tupleLength)]) for i in range(0, len(nrList), tupleLength)]

    [print(o) for o in out]
    return out

chk = genTuplesFromList()
# chk = genTuplesFromList(tupleLength=5)






