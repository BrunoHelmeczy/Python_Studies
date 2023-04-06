# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)
from itertools import product

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

['-'.join(x) for x in product(colors, sizes)]