# 3) Conditional Selection
import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(
    data = randn(5, 4),
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = 'W X Y Z'.split()
)

df[df > 0]          # Filtering via complete df
df[df['W'] > 0.5]   # via column condition

df[df['W'] > 0][['X']]
df[df['W'] > 0][['X', 'W']]

# 3.2) 2+ conditions; & / |
df[(df['W'] > -1) & (df['Z'] < 1)]
df[(df['W'] > 1) | (df['Z'] < 0)]


# 3.3) Play w Indices
df.reset_index()
# df.reset_index(inplace = True)

df['States'] = 'CA NY WY RO CO'.split()
df.set_index('States')

# 3.4) Multi-hierarchy indices
# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index_pd = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(
    data = np.random.randn(6, 2),
    index = hier_index_pd, 
    columns = ['A', 'B']
)

df.loc['G1']
df.iloc[[0]]
df.iloc[[1, 5]]

df.index.names = ['Grp', 'Nr']

df.loc['G2'].loc[2]['B']
df.iloc[4, 1]

df.xs('G1')
df.xs(1, level = 'Nr')
# df.xs(2, level = 'Nr')