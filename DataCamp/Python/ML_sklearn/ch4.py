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



# %%
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = ads_w_dummies1.drop('sales', axis = 1).values
y = ads_w_dummies1['sales'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size = 0.1, 
    random_state = 42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

from sklearn.linear_model import Ridge, Lasso, LinearRegression

ridge = Ridge(alpha = 0.1)
lasso = Lasso(alpha = 0.1)
linreg = LinearRegression()

ridge2 = Ridge(alpha = 0.1)
lasso2 = Lasso(alpha = 0.1)
linreg2 = LinearRegression()

models = {
    'ridge': ridge, 
    'lasso': lasso,
    'linreg': linreg,
    'ridge_scaled': ridge2,
    'lasso_scaled': lasso2, 
    'linreg_scaled': linreg2
}

data = {
    'x': {
        'raw': {
            'x_train': X_train,
            'x_test': X_test
        },
        'scaled': {
            'x_train': X_train_scaled,
            'x_test': X_test_scaled
        }
    }, 'y': {
        'y_train': y_train,
        'y_test': y_test
    }
}

# 1) fit

# m = models[4]
scores = {}

for item in models.items():
    if 'scaled' in item[0]:
        x_type = 'scaled'
    else:
        x_type = 'raw'
    
    x_train = data['x'][x_type]['x_train']
    x_test = data['x'][x_type]['x_test']
    y_train = data['y']['y_train']
    y_test = data['y']['y_test']

    item[1].fit(x_train, y_train)
    scores[item[0]] = item[1].score(x_test, y_test).round(4)

pd.DataFrame.from_dict(scores, orient = 'index', columns = ['accuracy'])


# %%
# in a pipeline + with cross-validation
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

steps = [
    ('scaler', StandardScaler()),
    ('ridge', Ridge())
]

pipeline = Pipeline(steps)

params = {
    'ridge__alpha': 10.0 ** np.arange(-5, 0, 0.1)
}

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size = 0.1, 
    random_state = 42
)

cv = GridSearchCV(pipeline, param_grid = params)

cv.fit(X_train, y_train)

# cv.best_estimator_
cv.best_params_
cv.best_score_

cv.score(X_test, y_test)

