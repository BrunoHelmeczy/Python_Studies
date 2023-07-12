import sys # sue for importing my_utils (á la other python modules)
import matplotlib.pyplot as plt
sys.path.append('../Python_Studies/DataCamp/Python/Time_Series')
from my_utils import *

checkFx()

# 4.1) select index comps + import data
nyse = pd.read_excel(
    getFilePaths('listings')[0],
    sheet_name = 'nyse',
    na_values = 'n/a'
)

nyse.info()
nyse.set_index('Stock Symbol', inplace = True)
nyse.dropna(subset = 'Sector', inplace = True)
nyse['Market Capitalization'] = nyse['Market Capitalization'] / 1e6

# select companies with largest market cap / sector
comps = nyse.groupby('Sector')['Market Capitalization'].nlargest(1)
comps.sort_values(ascending = False)

tickers = nyse.groupby('Sector')['Market Capitalization'] \
    .nlargest(1).index.get_level_values('Stock Symbol')

pd.options.display.float_format = '{:,.2f}'.format # set print format option for float Nrs
nyse.loc[tickers, :]

# pd.read_csv(
#     getFilePaths('stocks_4')[0]
# )

