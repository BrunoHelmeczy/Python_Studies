# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

mylist = ['Kate', 'Bruno', 'Benedek', 'Lili', 'Zsombi']

def my_enumerate(mylist):
      return [(x, mylist[x]) for x in range(len(mylist))]


my_enumerate(mylist)
list(enumerate(mylist))
