# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread = 'white', *args):
    out = [item for item in args]

    out.insert(0, bread + ' bread')
    out.append(bread + ' bread')

    return ' + '.join(out)

make_sandwich('multi-grain', 'ham', 'cheese', 'lettuce', 'tomato')