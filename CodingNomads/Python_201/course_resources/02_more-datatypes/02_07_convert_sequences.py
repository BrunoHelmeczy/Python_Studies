# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string  = "codingnomads"
stringT = tuple(string)
stringL = [l for l in stringT]
stringL[stringL.index('c')] = 'k'

stringT2 = tuple(stringL)

''.join(stringL)
''.join(stringT2)
