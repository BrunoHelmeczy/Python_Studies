import numpy as np

# Indexing & Selection
arr = np.arange(0, 11)

arr[0]
arr[1:]
arr[:3]
arr[1:3]
arr[1:4:2]
arr[1::2]
arr[:-1:2]

lst = list(range(11))

arr[:2] = 100 # same w list throughs error
# lst[:2] = 100

arrslice = arr[:6] 
arrslice[:] = 99 # updates by reference --> arr also affected

arrcopyslice = arr.copy()[6:]

arrcopyslice[:] = 101
arr

