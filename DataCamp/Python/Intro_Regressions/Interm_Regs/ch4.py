import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import logit
from itertools import product
from pathlib import Path
from os import listdir

def getData(csv_name):
    data_folder = Path().resolve().joinpath('DataCamp/Python/Intro_Regressions/data')
    csvs = listdir(data_folder)

    if csv_name not in csvs:
        csv_text = f'Select from these available files: \n{csvs}'
        data_text = f'Alternatively, move your file in the data folder: \n{data_folder}'

        return print(f'Error: "{csv_name}" is not present in the data folder. \n\n{csv_text} \n\n{data_text}\n')
    
    return pd.read_csv(
        data_folder.joinpath(csv_name)
    )

churn = getData('churn.csv')

cols = list(churn.columns)
Y = cols.pop(0)
form_txt = Y + ' ~ ' + ' * '.join(cols)

lm1 = logit(
    formula = form_txt,
    data = churn
).fit()

lm1.summary()
lm1.pred_table()

# 
exp_data = pd.DataFrame(
    product(
        np.arange(-2, 4.1, 0.1),
        np.arange(-1, 6.1, 0.1)
    ),
    columns = cols
)

pred_data = exp_data.assign(
    has_churned = lm1.predict(exp_data)
)

pred_data['most_likely'] = pred_data['has_churned'].round()

sns.scatterplot(
    x = "time_since_first_purchase",
    y = "time_since_last_purchase",
    data = churn, 
    hue = "has_churned"
)

sns.scatterplot(
    x = "time_since_first_purchase",
    y = "time_since_last_purchase",
    data = pred_data,
    hue = 'most_likely',
    alpha = 0.2,
    legend = False
)

plt.show()

conf_matrix = lm1.pred_table()

TN = conf_matrix[0, 0]
TP = conf_matrix[1, 1]
FN = conf_matrix[1, 0]
FP = conf_matrix[0, 1]

accuracy = sum([TN, TP]) / sum([TN, TP, FN, FP])
sensitivity = sum([TP]) / sum([ TP, FN]) # % of true positives
specificity = sum([TN]) / sum([ TN, FP]) # % of true negatives


# distributions 
from scipy.stats import norm

x = np.arange(-4, 4.05, 0.05)

gauss_dist = pd.DataFrame({
    'x': x,
    'norm_pdf': norm.pdf(x),
    'norm_cdf': norm.cdf(x)
})

sns.lineplot(
    x = 'x',
    y = 'norm_pdf',
    data = gauss_dist
)

sns.lineplot(
    x = 'x',
    y = 'norm_cdf',
    data = gauss_dist
)

plt.show()

# inverse of cdf (quantile f(x))

p = np.arange(0.001, 1, 0.001)

gauss_inv = pd.DataFrame({
    'p': p,
    'norm_inv_cdf': norm.ppf(p)
})

sns.lineplot(
    x = 'p',
    y = 'norm_inv_cdf',
    data = gauss_inv
)
plt.show()

# logistic dist
from scipy.stats import logistic as lg

logit_dist = pd.DataFrame({
    'x': x,
    'log_pdf': lg.pdf(x)
})

sns.lineplot(
    x = 'x',
    y = 'log_pdf',
    data = logit_dist
)
plt.show()

# logit function = logistic cdf(x) = 1 / (1 + exp(-x))
    # inverse cdf: log(p / (1 - p))

# lg.ppf(p)
