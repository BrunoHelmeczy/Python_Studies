import numpy as np
import pandas as pd
from pathlib import Path

# 1) read in ecomm purch dat as pd.DataFrame()
filename = next(Path.cwd().rglob('Ecommerce Purchases'))
ecom = pd.read_csv(filename)

# 2) check head() / shape
ecom.head()
rows, cols = ecom.shape

# 3-4) min, avg, max purchase prices
ecom[['Purchase Price']].agg(
    [min, np.mean, np.median, max]
)

# 5) nr pax w 'en' as lang choice
ecom[ecom['Language'] == 'en'].shape[0]
# ecom.groupby('Language').count() 

# 6) nr pax w job title 'Lawyer'
ecom[ecom['Job'] == 'Lawyer'].shape[0] 

# 7) nr AM vs PM purchases
ecom.groupby('AM or PM').size()

# 8) 5 most common job titles ?
ecom.groupby('Job').size().sort_values(ascending = False).head(5)
ecom['Job'].value_counts().head(5)

# 9) search Lot == '90 WT' --> purchase price ?
ecom[ecom['Lot'] == '90 WT']['Purchase Price'].iloc[0]

# 10) email of pax w cc nr: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853].loc[:, 'Email']

# 11) nr pax w amex cc provide + made purchase > 95
ecom[(ecom['Purchase Price'] > 95) & (ecom['CC Provider'].str.lower().str.contains('express'))].shape[0]

# 12) nr pax w cc exp in 2025
ecom[(ecom['CC Exp Date'].str.extract(r"/(.+)$") == '25').loc[:, 0]].shape[0]

# 13) top 5 email providers
ecom['email_provider'] = ecom['Email'].str.extract(r'@(.+)$')

ecom.groupby('email_provider').size().sort_values(ascending = False).head(5)
