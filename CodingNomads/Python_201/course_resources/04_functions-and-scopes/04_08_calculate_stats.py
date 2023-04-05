# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(nrs = example_list):
    Min = min(nrs)
    Max = max(nrs)
    Sum = sum(nrs)
    Mean = Sum / len(nrs)

    out = {'min': Min, 'max': Max, 'mean': Mean, 'sum': Sum }

    print(f"Input: {nrs} \nOutput Summary:")

    [print(f"{k}: {v}") for k, v in out.items()]

    return out

stats()