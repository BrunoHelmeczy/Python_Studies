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
    # .expanding() ~ .rolling()
    # spec shorthands: cumsum/prod/min/max/ etc.
df = pd.DataFrame({'data': range(1, 5)}) 
df['data'].expanding().sum()
df['data'].cumsum()
df['data'].cummax()
df['data'].cummin()
df['data'].cumprod()

df['data'].expanding().agg( # product not working (?)
    ['min', 'max', 'mean', 'median', 'std']
)

data = pd.read_csv(
    getFilePaths('sp500')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

data.pct_change().add(1).SP500.cumprod().sub(1).plot(); plt.show()

# rolling annual rate of return
def multi_period_return(period_returns):
    return np.prod(period_returns + 1) - 1

data['Rolling_1yr_ARR'] = data['SP500'].pct_change().rolling('360D').apply(multi_period_return).mul(100)

data['Rolling_1yr_ARR'].plot(); plt.show()

# 3.2) exercises
# 3.2.1)
goog = pd.read_csv(
    getFilePaths('google')[0],
    names = ['date', 'price'],
    header = 0,
    parse_dates = ['date'],
    index_col = 'date'
).asfreq('B').dropna()


start = goog.first('D')

goog.equals(
    pd.concat(
        [start, goog.diff().dropna()]
    ).cumsum()
)

# 3.2.2)
data = pd.read_csv(
    getFilePaths('apple_google')[0],
    parse_dates = ['Date'],
    index_col = 'Date'
).loc['2010-12-16':]

inv = 1000

data.pct_change().add(1).cumprod().mul(inv).plot(); plt.show()

# 3.2.3)
# multi_period_return

# 3.3) price simulation
# gen random nrs
from numpy.random import normal, seed, choice
from scipy.stats import norm 

seed(42)
rnd_rets = normal(loc = 0, scale = 0.01, size = 1000)

import seaborn as sns
sns.distplot(
    rnd_rets,
    fit = norm,
    kde = False
)
plt.show()

pd.Series(rnd_rets).add(1).cumprod().sub(1).mul(100).plot(); plt.show()

data = pd.read_csv(
    getFilePaths('sp500')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

data['returns'] = data['SP500'].pct_change()

data.plot(subplots = True); plt.show()

sns.distplot(
    data.returns.dropna().mul(100),
    fit = norm
)
plt.show()

rw = choice(
    data['returns'].dropna(),
    size = data['returns'].count() 
)


sp500_rnd = pd.concat([
    data['SP500'].first('D'),
    pd.Series(rw, index = data.dropna().index).add(1)
])

data['sp500_rnd'] = sp500_rnd.cumprod()
data.plot(); plt.show()

# 3.3) exercises
# 3.3.1)
seed(42)

rw = normal(
    loc = 0.001, 
    scale = 0.01,
    size = 2500
)

pd.Series(rw).add(1).cumprod().mul(1000).plot(); plt.show()

# 3.3.2)
fb = pd.read_csv(
    getFilePaths('fb')[0],
    names = ['date', 'price'],
    parse_dates = ['date'],
    index_col = 'date'
)

# 3.4) ts correlations
data = pd.read_csv(
    getFilePaths('asset')[0],
    parse_dates = ['DATE'],
    index_col = 'DATE'
).dropna()

data.info()

sns.jointplot(
    x = 'SP500',
    y = 'Bonds',
    data = data.pct_change()
)
plt.show()

data.corr()
data.pct_change().corr()


data.agg(np.log, axis = 0).diff().plot(subplots = True); plt.show()

sns.heatmap(
    data = data.agg(np.log, axis = 0).diff().corr().abs(),
    annot = True
)
plt.show()

# 3.4) exercises
# 3.4.1)
data = pd.read_csv(
    getFilePaths('5_stocks')[0],
    parse_dates = ['Date'],
    index_col = 'Date'
).dropna()

data.info()

sns.heatmap(
    data = data.resample('A').last().pct_change().corr().abs(),
    annot = True
)
plt.show()

