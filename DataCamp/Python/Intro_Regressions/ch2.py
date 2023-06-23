import numpy as np
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

# generate predictions
exp_data = pd.DataFrame(
    {'n_convenience': np.arange(0, 11)}
)

pred_data = exp_data.assign(
    price_twd_msq = lm_model.predict(exp_data)
)

# assign as new column on model data
taiwan_real_estate = taiwan_real_estate.assign(
    price_twd_msq_fc = lm_model.predict(taiwan_real_estate)
)

# viz predictions & actuals
fig = plt.figure()

taiwan_real_estate.columns
sns.regplot(
    x = 'n_convenience',
    y = 'price_twd_msq',
    ci = None,
    data = taiwan_real_estate
)

sns.scatterplot(
    x = 'n_convenience',
    y = 'price_twd_msq_fc',
    data = taiwan_real_estate,
    color = 'red',
    marker = 's'
)
plt.show()

# Info extraction fr models

# coefficients
lm_model.params

# fitted values
# same as lm_model.predict(taiwan_real_estate) 
lm_model.fittedvalues

# residuals: Y-actuals - fittedvalues
lm_model.resid

# Summary of results: Rsq + similar stats + coeffs & P-values
lm_model.summary()

# 