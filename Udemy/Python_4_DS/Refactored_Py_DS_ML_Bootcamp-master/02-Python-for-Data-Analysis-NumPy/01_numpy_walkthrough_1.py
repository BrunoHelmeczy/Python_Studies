import numpy as np

# 1) create array / matrix from lists
lst = [1, 2, 3]
np_array = np.array(lst)

mat = [lst, lst, lst]
np_mat = np.array(mat)

# 2) Generate directly
np.arange(0, 10) # [1, 2, ..., 9]
np.arange(0, 10, 2) # [0, 2, ..., 8]

# 3) 0s, 1s, Linear Space 
np.zeros(3)
np.zeros((3, 3))

np.ones(3)
np.ones((3, 3))

np.linspace(0, 10, 6)

# 4) identity matrix
np.eye(4) # default to N^2 matrix
np.eye(4, 10) # N * M matrix --> 4 * 10
np.eye(4, 5, 1)

# 5) gen random Nrs

# uniform
np.random.random(4)
np.random.rand(4)
np.random.rand(4, 4)

# normal
rnorm = np.random.normal(100, 15, 100)
rnorm.max()

# standard normal
np.random.randn()
np.random.randn(5)
np.random.randn(5, 5)

# random ints
np.random.randint(0, 2, 10)
np.random.randint(0, 2, (10, 10)) # 2d
np.random.randint(0, 2, (3, 3, 3)) # 3d


# 6) Attributes & Methods
arr = np.arange(25)
ranarr = np.random.randint(0, 6, (5, 5))

arr.reshape(5, 5)
ranarr.reshape(1, 25)


arr.argmax()
arr.argmin()
arr.max()
arr.min()

arr.shape
ranarr.shape

arr.dtype
ranarr.dtype