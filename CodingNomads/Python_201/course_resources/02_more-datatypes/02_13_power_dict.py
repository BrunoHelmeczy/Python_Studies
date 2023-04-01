# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

def genNsquaredDict(N = 10):
    return {n: n ** 2 for n in range(1, N + 1)}

genNsquaredDict(100)
