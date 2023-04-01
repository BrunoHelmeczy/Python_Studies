# Write code that creates a list of all unique values in a list.
# For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [x for x in set(list_)]

def getUniqueList(listIn):
    return [x for x in set(listIn)]