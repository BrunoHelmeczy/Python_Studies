import timeit
import numpy as np

ListComp = "[x for x in range(10)]"
GenComp = "(x for x in range(10))"

np.mean(timeit.repeat(ListComp)) # Avg: 0.45
np.mean(timeit.repeat(GenComp))  # Avg: 0.39

def getList():
    return [x for x in range(10)]

def getGen():
    return (x for x in range(10))  

setup = """
List = [x for x in range(1000)]
Gen  = (x for x in range(1000))
"""

np.mean(timeit.repeat("[x for x in List]", repeat = 10, number = 10000, setup = setup)) # avg: 0.24
np.mean(timeit.repeat("[x for x in Gen]" , repeat = 10, number = 10000, setup = setup)) # avg: 0.0015 (x160)

lam_sq = lambda x: x ** 2
lam_sq(3)
