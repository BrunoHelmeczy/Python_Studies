import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols, logit
# from statsmodels.formula.api import logit
from pathlib import Path

data_folder = Path().resolve().joinpath('DataCamp/Python/Intro_Regressions/data')

churn = pd.read_csv(
    data_folder.joinpath('churn.csv')
)

# OLS - predictions can go outside 0-1 range...
lm_churn = ols(
    formula = 'has_churned ~ time_since_last_purchase',
    data = churn
).fit()

intercept, slope = lm_churn.params

sns.scatterplot(
    x = 'time_since_last_purchase',
    y = 'has_churned',
    data = churn
)
plt.axline(
    xy1 = (0, intercept), 
    slope = slope
)
plt.xlim(-10, 10)
plt.ylim(-0.2, 1.2)

plt.show()

# logit
logit_churn = logit(
    formula = 'has_churned ~ time_since_last_purchase',
    data = churn
).fit()

logit_churn.params

logit_churn_1st = logit(
    formula = 'has_churned ~ time_since_first_purchase',
    data = churn
).fit()

sns.regplot(
    x = 'time_since_last_purchase',
    y = 'has_churned',
    data = churn,
    ci = None,
    logistic = True
)

plt.axline(xy1 = (0, intercept), slope = slope, color = 'black')
plt.xlim(-10, 10)
plt.ylim(-0.2, 1.2)

plt.show()

# faceted histograms
sns.displot(
    x = 'time_since_last_purchase',
    data = churn,
    col = 'has_churned'
)
plt.show()

# grouped histogram
sns.histplot(
    x = 'time_since_last_purchase',
    data = churn,
    hue = 'has_churned',
    alpha = 0.3 ,
    element = 'step'
)
plt.show()

sns.regplot(
    x = 'time_since_first_purchase',
    y = 'has_churned',
    data = churn,
    ci = None,
    line_kws = {'color': 'red'}
)
sns.regplot(
    x = 'time_since_first_purchase',
    y = 'has_churned',
    data = churn,
    ci = None,
    logistic = True,
    line_kws = {'color': 'blue'}
)
plt.show()

# gen predictions
exp_data = pd.DataFrame(
    {'time_since_first_purchase': np.arange(-1.5, 4.1, 0.25)}
)

pred_data = exp_data.assign(
    has_churned_fc = logit_churn_1st.predict(exp_data)
)

# vis
fig = plt.figure()
sns.regplot(
    x = 'time_since_first_purchase',
    y = 'has_churned_fc',
    data = pred_data,
    ci = None,
    logistic = True
)
plt.show()

# quant assess logit reg fit
    # confusion matrix
acts = churn['has_churned']
pred = np.round(logit_churn_1st.predict())

out = pd.DataFrame({
    'actuals': acts,
    'predicted': pred
})

out.value_counts(sort = False)

conf_matrix = logit_churn_1st.pred_table()
    # true  negative; false positive;
    # false negative; true  positive

# plot conf matrix
from statsmodels.graphics.mosaicplot import mosaic

plot = mosaic(conf_matrix, axes_label = True)

# plot.set(
#     xlabel = 'Actual Response',
#     ylabel = 'Predicted Response'
# )

# plt.xlabel('Actual Response')
# plt.ylabel('Predicted Response')
plt.show()

# metrics:
    # accuracy: True values / all values
TN = conf_matrix[0, 0]
TP = conf_matrix[1, 1]
FN = conf_matrix[1, 0]
FP = conf_matrix[0, 1]

accuracy = sum([TN, TP]) / sum([TN, TP, FN, FP])
sensitivity = sum([TP]) / sum([ TP, FN]) # % of true positives
specificity = sum([TN]) / sum([ TN, FP]) # % of true negatives
