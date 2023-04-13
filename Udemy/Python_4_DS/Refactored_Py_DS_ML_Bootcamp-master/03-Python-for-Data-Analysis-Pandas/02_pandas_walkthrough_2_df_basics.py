import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)

# 2) Dataframes
df = pd.DataFrame(
    data = randn(5, 4),
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = 'W X Y Z'.split(' ')
)

df['W']
type(df['W'])

df[['W']]
type(df[['W']])

df[['W', 'Z']]

df['new'] = df['W'] + df['Y']

df.drop('E', axis = 0) # drop 'E' row
df.drop('new', axis = 1) # drop 'new' column

df.drop('E', axis = 0, inplace = True)
df.drop('new', axis = 1, inplace = True)

# 2.1) Row selections --> .loc() / .iloc()
# as series
df.loc['A']
type(df.loc['A'])

df.iloc[0]
type(df.iloc(1))

# as df
df.iloc[[1]]
type(df.iloc[[0]])

# multi-select
df.loc[['A','B']]
df.iloc[list(range(0, 4, 2))]

# 2.2) Row + Col selections
df.loc['B', 'Y']
df.iloc[1, 2]

df.loc[["A", 'B'], ['X', 'Z']]
df.iloc[[2, 3],[ 1, -1]]