import numpy as np

# 1) Indexing & Selection
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

# 2D ARRAYS
arr2d = np.arange(0,25).reshape(5, 5)

arr2d[:2, 2:]

arr2d[arr2d > 10]

# 2) Operations
arr + arr
arr - arr
arr * arr
arr / (arr+1)
(arr+1) // arr
arr % (arr+1)

arr2d + arr2d
arr2d *2
arr2d ** 2
arr2d ** arr2d

np.sqrt(arr)
np.sqrt(arr2d)

np.exp(arr)
np.exp(arr2d)

np.sin(arr)
np.sin(arr2d)

np.log(arr)
np.log(arr2d + 0.01)

np.max(arr)
np.max(arr2d)
