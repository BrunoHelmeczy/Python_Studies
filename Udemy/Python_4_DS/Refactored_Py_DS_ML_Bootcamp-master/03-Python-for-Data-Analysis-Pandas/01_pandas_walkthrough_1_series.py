import pandas as pd
import numpy as np

# 1) pd Series --> 1-dimensional arrays / lists / dict
labels = ['a', 'b', 'c']
lst = [10, 20, 30]
arr = np.array(lst)

# arr2d = np.arange(9).reshape(3, 3)


d = dict(zip(labels, lst))
# d = {labels[i]: lst[i] for i in range(len(lst))}

pd.Series(data = lst)
pd.Series(data = lst, index = labels)
pd.Series(data = labels)
pd.Series(data = arr)
pd.Series(data = arr, index = labels)
pd.Series(data = arr, dtype = np.int8)
pd.Series(data = d)

# 1.2) Indexing 
ser1 = pd.Series(range(4), index = ['USA', 'Germany', 'USSR', 'Japan'])
ser1['USA']

ser2 = pd.Series(range(1, 5), index = ['USA', 'Germany', 'Italy', 'Japan'])
ser2['Italy']

ser3 = pd.Series(range(4))
ser3[3]

ser4 = pd.Series(['USA', 'Germany', 'Italy', 'Japan'])
ser4[3]

ser1 + ser2 # adding series by indices
