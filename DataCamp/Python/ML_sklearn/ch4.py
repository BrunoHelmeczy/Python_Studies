# %%
REL_PATH = 'DataCamp/Python/ML_sklearn'
import sys
sys.path.append(REL_PATH)
from my_utils import *

import os
print(os.getcwd())

dfs = getData(all = True)

print('hi')
# %%
# Pre-processing Data
ads = dfs['advertising_and_sales_clean']

ads['influencer'].value_counts()

ads_w_dummies = pd.concat([
    ads.drop('influencer', axis = 1),
    pd.get_dummies(ads['influencer'], prefix = 'inf', drop_first = True, dtype = int)
], axis = 1)

ads_w_dummies1 = pd.get_dummies(ads, drop_first = True, dtype = int)


