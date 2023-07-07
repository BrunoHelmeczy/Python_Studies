import sys # sue for importing my_utils (á la other python modules)
from datetime import datetime
import matplotlib.pyplot as plt
sys.path.append('../Python_Studies/DataCamp/Python/Time_Series')
from my_utils import *

checkFx()
# ck = getData('nyc.csv')

# 2.1) Compare TS growth rates
# df = getGoogleStockData()

filepath = getFilePaths('google.csv')[0]

goog = pd.read_csv(
    filepath,
    names = ['date', 'price'],
    header = 0,
    parse_dates = ['date'],
    index_col = 'date'
).asfreq('B')

first_price = goog.price.iloc[0]

goog['price'].div(first_price).multiply(100).plot(); plt.show()

prices_path = getFilePaths('stock_data.csv')[0]

# pd.read_csv(getFilePaths('5_stocks.csv')[0])
# pd.read_csv(getFilePaths('stocks_4.csv')[0])
prices = pd.read_csv(
    prices_path, 
    parse_dates = ['Date'],
    index_col = 'Date'
)

normed = prices.div(prices.iloc[0])

sp500 = pd.read_csv(
    getFilePaths('sp500.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
).loc['2010':]

sp500.div(sp500.iloc[0])
normed

prices = pd.concat([normed, sp500.div(sp500.iloc[0])], axis = 1).dropna()

prices.plot(); plt.show()
 
prices[normed.columns].sub(prices['SP500'], axis = 0).plot(); plt.show()

# 2.1) Exercises
# 2.1.1)
prices = pd.read_csv(
    getFilePaths('asset_classes.csv')[0],
    parse_dates = ['DATE'],
    index_col = 'DATE'
)


normed = prices.div(prices.iloc[0]).mul(100)
normed.plot(); plt.show()

# 2.1.2)
stocks = pd.read_csv(
    getFilePaths('nyse.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

dj = pd.read_csv(
    getFilePaths('dow_jones.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

df = pd.concat([stocks, dj], axis = 1)

df.div(df.iloc[0]).mul(100).plot(); plt.show()

# 2.1.3)
tickers = ['MSFT', 'AAPL']

stocks = pd.read_csv(
    getFilePaths('msft_aapl.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

sp500 = pd.read_csv(
    getFilePaths('sp500.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

df = pd.concat([stocks, sp500], axis = 1).dropna()

norm = df.div(df.iloc[0]).mul(100)

norm[tickers].sub(norm['SP500'], axis = 0).plot(); plt.show()

# 2.2) Change ts frequency
# upsampling (weekly --> daily) --> fill/interpolate missing data
# downsample (daily --> weekly) --> aggregate existing data
# pd methods: asfreq(); reindex(); resample()

Qs = pd.Series(
    data = range(1, 5),
    index = pd.date_range(start = '2016', periods = 4, freq = 'Q')
)

monthly = Qs.asfreq('M').to_frame('baseline')

monthly['ffill'] = Qs.asfreq('M', method = 'ffill')
monthly['bfill'] = Qs.asfreq('M', method = 'bfill')
monthly['value'] = Qs.asfreq('M', fill_value = 0)

# add missing months at start
Ms = pd.date_range(start = '2016', periods = 12, freq = 'M')

monthly.reindex(Ms)

Qs.reindex(Ms).to_frame('baseline')

# 2.2) Exercises
# 2.2.1) 
start = '2016-01-01'
end = '2016-02-29'

mnth_data = pd.date_range(start = start, end = end, freq = 'M')

monthly = pd.Series(
    data = [1, 2],
    index = mnth_data
)

wk_dates = pd.date_range(start = start, end =end, freq = 'W')

monthly.reindex(wk_dates, method = 'bfill')
monthly.reindex(wk_dates, method = 'ffill')


# 2.2.2)
df = pd.read_csv(
    getFilePaths('unrate_2000.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

df.asfreq('W', method = 'ffill')['2015':].plot(); plt.show()

# 2.3) Upsample interpolation w .resample()
# .resample() ~ .groupby()
unrate = pd.read_csv(
    getFilePaths('unrate_2000.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

# unrate.info()
unrate.asfreq('M')
unrate.asfreq('MS')
unrate.asfreq('BM')
unrate.asfreq('BMS')

# assert equality
unrate.asfreq('MS').equals(unrate.resample('MS').asfreq())

gdp = pd.read_csv(
    getFilePaths('gdp_growth.csv')[0],
    parse_dates = ['date'],
    index_col = 'date'
)

gdp.info()

gdp1 = gdp.resample('MS').ffill().add_suffix('_ffill')
gdp2 = gdp.resample('MS').interpolate().add_suffix('_inter')

pd.concat([gdp1, gdp2], axis = 1).plot(); plt.show()
pd.concat([unrate, gdp2], axis = 1)['2007':'2017-01'].plot(); plt.show()

