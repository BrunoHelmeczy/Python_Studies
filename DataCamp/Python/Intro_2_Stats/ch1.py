import numpy as np

np.linspace(0, 1, 6)

rands = np.random.normal(100, 15, 1000)

np.quantile(rands.round(2), np.linspace(0, 1, 6)) 
np.quantile(rands.round(2), [0, 0.2, 0.4, 0.6, 0.8, 1])

# ch3
from scipy.stats import norm
import pandas as pd

IQs = norm.rvs(100, 15, size = 10000)
txt = [w for w in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
names = np.random.choice(txt, 10000, replace = True)

df = pd.DataFrame({
    'name': names,
    'iq': IQs
})

sampling_dist = [np.mean(df['iq'].sample(20, replace = True)).round(2) for i in range(20)]

from scipy.stats import poisson

poisson.pmf(5, 4)

