import sys # sue for importing my_utils (á la other python modules)
sys.path.append('../Python_Studies/DataCamp/Python/Time_Series')
from my_utils import *

checkFx()
ck = getData('nyc.csv')

from datetime import datetime

# 1.1) Timestamps
dt = datetime(2023, 1, 1)
ts1 = pd.Timestamp(dt)
ts2 = pd.Timestamp('2023-01-01')

assert ts1 == ts2 # True

ts1.year
ts1.month
ts1.month_name()
ts1.day
ts1.day_name()
ts1.day_of_week
ts1.day_of_year
ts1.date()

ts1.to_period('D')

# 1.2) Periods 
per_mnt = pd.Period('2023-01') # period + frequency (default: Month = 'M')
pd.Period('2023-01-01')

per_mnt.asfreq('D') # default: end of month
per_mnt.asfreq('D', 'start')
per_mnt.asfreq('Y')

per_mnt.to_timestamp()
per_mnt.asfreq('D', 'start').to_timestamp()
per_mnt.asfreq('D').to_timestamp()

(per_mnt + 2).asfreq('D')

# 1.3) Time Series
# pd.date_range() start, end, periods, freq (must spec exactly 3 of 4)
index = pd.date_range(
    start = '2023-01-01',
    end = datetime.today(),
    freq = 'D'
)

index.to_period()

# 1.4) into pd.DataFrame()-s: use timestamps/periods as Index
pd.DataFrame({'data': index}).info()

import numpy as np

data = np.random.random(size = (12, 2))

index = pd.date_range(
    start = '2023-01-01',
    periods = 12,
    freq = 'M'
)

pd.DataFrame(data = data, index = index)


# 2) Indexing & Resampling

