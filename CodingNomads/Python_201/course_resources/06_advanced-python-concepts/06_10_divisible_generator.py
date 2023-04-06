# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 1000000)

gen = (x-1 for x in range(1, 1000001, 1111) if x != 1)

[print(x) for x in gen]