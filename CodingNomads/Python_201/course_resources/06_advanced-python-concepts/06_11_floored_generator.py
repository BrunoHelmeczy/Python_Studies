# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?
gen2 = (((x - 1) // 1111) for x in range(1, 1000000, 1111) if x != 1 )

[x for x in gen2]