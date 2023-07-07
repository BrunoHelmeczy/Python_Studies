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
