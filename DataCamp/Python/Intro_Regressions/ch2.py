import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from pathlib import Path

data_folder = Path().resolve().joinpath('DataCamp/Python/Intro_Regressions/data')

taiwan_real_estate = pd.read_csv(
    data_folder.joinpath('taiwan_real_estate2.csv')
)

# create model object
lm_model = ols(
    formula = 'price_twd_msq ~ n_convenience',
    data = taiwan_real_estate
)

# fit lm_model object
lm_model = lm_model.fit()

# check coeffs ~ params
lm_model.params

# EDA
sns.displot(
    x = 'price_twd_msq',
    data = taiwan_real_estate,
    col = 'house_age_years',
    bins = 10
)
plt.show()

# Categorical X-vars --> 1 of values removed by default (1st occurring ?)
lm_age = ols(
    formula = 'price_twd_msq ~ house_age_years + n_convenience',
    data = taiwan_real_estate
).fit()

lm_age.params