# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

list_ = starter_list = [0, [1, 2, 3, 4], [5, 6], [7, 8, 9], [10, [11, 12, [13, 14, [15, [16, [17]]]]]]]

list2 = []
for sublist in list_:
    for item in sublist:
        list2 += [item]

[item for sublist in list_ for item in sublist]

def flatten(list_):
    end = []
    [end.extend(s) if isinstance(s, list) else end.append(s) for s in list_]

    if max([isinstance(s, list) for s in end]):
        return flatten(end)
    else:
        return end

flatten(list_)