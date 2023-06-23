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

# fitted values - same as lm_model.predict(taiwan_real_estate) 
lm_model.fittedvalues

# residuals: Y-actuals - fittedvalues
lm_model.resid

# Summary of results: Rsq + similar stats + coeffs & P-values
lm_model.summary()

# Model fit attributes
lm_model.rsquared
lm_model.mse_resid # MSE
lm_model.mse_resid ** 0.5 # Residual Standard Error

# RMSE
np.sqrt(sum(lm_model.resid ** 2) / len(lm_model.resid))

# model fit visualizations
# residuals vs fitted
# lm_model.params
plot = sns.residplot(
    x = 'n_convenience',
    y = 'price_twd_msq',
    data = taiwan_real_estate,
    lowess = True
)

plot.set(
    xlabel = 'Fitted Values',
    ylabel = 'Residuals'
)
plt.show()

# Q-Q plot

## %%

from statsmodels.api import qqplot
qqplot(
    data = lm_model.resid,
    fit = True,
    line = '45'
)
plt.show()

## %%
# Scale location plot:
    # x: fitted values
    # y: sqrt(standardized residuals)
    
    # normalized residuals
lm_norm_resids = lm_model.get_influence().resid_studentized_internal 
Y = np.sqrt(np.abs(lm_norm_resids))

plot = sns.regplot(
    x = lm_model.fittedvalues,
    y = Y,
    ci = None,
    lowess = True
)
plot.set(
    xlabel = 'Fitted Values',
    ylabel = 'Sqrt(Normalized Residuals)'
)

plt.show()

# Outliers, leverage, influence
model_summ_frame = lm_model.get_influence().summary_frame()

taiwan_real_estate['leverage'] = model_summ_frame['hat_diag']

