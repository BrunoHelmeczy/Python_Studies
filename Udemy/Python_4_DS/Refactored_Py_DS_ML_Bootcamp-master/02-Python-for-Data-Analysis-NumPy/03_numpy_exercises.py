import numpy as np

# 1) array 10 0s
np.zeros(10)

# 2) array of 10 1s
np.ones(10)

# 3) array of 10 5s
np.ones(10) * 5

# 4) array of integers 10:15
np.arange(10, 51)

# 5) 4) with only even nrs
np.arange(10, 51, 2)

# 6) 3x3 matrix w values 0:8
np.arange(9).reshape(3, 3)

# 7) identity matrix 3x3
np.eye(3, 3)

# 8) gen rnadom nr 0-1
np.random.random()
np.random.rand()

# 9)  25 rand nrs fr standard normal dist
np.random.randn(5, 5)

# 10) 10x10 matrix fr 0.01 to 1
np.linspace(0.01, 1., 100).reshape(10, 10)

# 11) 20 evenly space nrs 0-1
np.linspace(0, 1, 20)

# 12) matrices - slicing / selection
mat = (np.arange(25) + 1).reshape(5, 5)

mat[2:, 1:]
mat[3, 4]
mat[:3, 1].reshape(3, 1)
mat[4]
mat[3:]

# 13) array calcs
mat.sum()
mat.std()

mat.sum(axis = 0) # 0 = columns
mat.sum(axis = 1) # 1 = rows
