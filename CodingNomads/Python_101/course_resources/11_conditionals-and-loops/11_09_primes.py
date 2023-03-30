# Print out every prime number between 1 and 1000.
# loop through nrs
# check if prime --> Y: print
from itertools import compress 

def isPrime(nr = 2):
    rt = int(nr ** (1/2)) + 1

    if nr < 2:
        return False
    elif nr == 2:
        return True

    for i in range(2, rt + 1):
        if (nr % i == 0):
            return False
    return True

def getPrimes(min = 0, max = 100):
    Range = range(min, max + 1)

    return list(compress(Range, [isPrime(x) for x in Range]))

getPrimes(max = 1000)



    

