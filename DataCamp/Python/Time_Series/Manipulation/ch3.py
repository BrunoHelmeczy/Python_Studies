import sys # sue for importing my_utils (á la other python modules)
import matplotlib.pyplot as plt
sys.path.append('../Python_Studies/DataCamp/Python/Time_Series')
from my_utils import *

checkFx()

# 3.1) rolling window fx()s w pandas
df = pd.read_csv(
    getFilePaths('google')[0],
    names = ['date', 'price'],
    parse_dates = ['date'],
    index_col = 'date',
    header = 0
).interpolate()

df.plot(); plt.show()

# integer-based 
df.rolling(window = 30).mean()
df.rolling(
    window = 30, 
    min_periods = 2 # smallest window size to still calculate with
).mean()

# offset-based window size
df.rolling(
    window = '30D' # no need for min window size
).mean()

df.join(
    df.rolling('90D').mean().add_suffix('_ma90')
)

df.assign(
    MA30 = df.rolling('30D').mean(),
    MA90 = df.rolling('90D').mean(),
    MA360  = df.rolling('360D').mean()
).plot()
plt.show()

df.price.rolling('90D').agg(['mean', 'std']).plot(subplots = True); plt.show()

df.rolling('360d').agg(
    ['mean', 'median']
)

roll = df.rolling('360D')

df.assign(
    q10_M360 = roll.quantile(0.1),
    q90_M360 = roll.quantile(0.9)    
).plot(); plt.show()

roll.agg(
    func = ['mean', 'std', lambda x: x.quantile(0.1)]
).rename(columns = {'<lambda>': 'q10'})

# 3.1) exercises
# 3.1.1)
# ...

# 3.2) expanding window fx()s - cumsum, etc.
