# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

# from resources import randlist

# import resources

# resources.randlist([1,2,3, 4,5])
# resources.randlist(2, 1)

# print(randlist)
from random import randint
import numpy
UI = input('press a number \n')
UI = int(UI)

Nrs = [randint(-100, 100) for x in range(UI)]

print(f"You selected to use {UI} Nrs. They are: {Nrs} \nTheir Product is: {numpy.product(Nrs)}")




