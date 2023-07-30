# %%
REL_PATH = 'DataCamp/Python/ML_sklearn'
import sys
sys.path.append(REL_PATH)
from my_utils import *

import os
os.getcwd()

dfs = getData(all = True)

# %%
diabetes = dfs['diabetes_clean']
X = diabetes.drop('glucose', axis = 1).values
y = diabetes['glucose'].values

# diabetes.head()

# %%
import plotly.express as px

px.scatter(
    data_frame = diabetes,
    x = 'bmi',
    y = 'glucose'
).update_layout(
    xaxis = {'title': 'Body Mass Index'}
    , yaxis = {'title': 'Blood Glucose (mg/dl)'}
)

# %%

X_bmi = diabetes[['bmi']].values
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X_bmi, y)

y_pred = reg.predict(X_bmi)

df = pd.DataFrame({
    'bmi':X_bmi.flatten(),
    'glucose_pred': y_pred
})

# %%
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(    
    go.Scatter(
        x = diabetes['bmi'],
        y = y,
        name = 'Actual',
        mode = 'markers'
    )
).add_trace(
    go.Scatter(
        x = df['bmi'],
        y = df['glucose_pred'],
        name = 'Predicted'
    )
)

# %%
# 2.2) MLR

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = diabetes.drop('diabetes', axis = 1).values
y = diabetes['diabetes'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    random_state = 42, 
    test_size = 0.3,
    stratify = y
)

reg = LinearRegression().fit(X_train, y_train)
y_pred = reg.predict(X_test)

reg.score(X_test, y_test) # R-squared

from sklearn.metrics import mean_squared_error

mean_squared_error(y_test, y_pred) # squared = True (default) --> MSE
mean_squared_error(y_test, y_pred, squared = False) # squared = False --> RMSE


# %%
# 2.3) Cross Validation
from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits = 5, shuffle = True, random_state = 42)

reg = LinearRegression()

cv_train = cross_val_score(reg, X_train, y_train, cv = kf)
cv_all   = cross_val_score(reg, X, y, cv = kf)

np.mean(cv_train).round(3)
np.std(cv_train).round(3)
np.mean(cv_all).round(3)
np.std(cv_all).round(3)

# %%
sales_df = dfs['advertising_and_sales_clean']
X = sales_df.drop(['sales', 'influencer'], axis = 1).values
y = sales_df['sales'].values

kf = KFold(n_splits = 5, shuffle = True, random_state = 42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    random_state = 42, 
    test_size = 0.1
    # stratify = y # only for classification problems
)
reg = LinearRegression()
cv_scores = cross_val_score(
    reg, 
    X_train, y_train,
    cv = kf
)

np.mean(cv_scores).round(3)
np.std(cv_scores).round(3)
np.quantile(cv_scores, [0.025, 0.975]).round(3)


# %%
# 2.4) Regularized Regressions: Ridge(): Lasso()
from sklearn.linear_model import Ridge

alphas = 10 ** np.arange(-1.0, 4.0)

def get_ridge_scores(alpha, X_train, X_test, y_train, y_test):
    ridge = Ridge(alpha = alpha).fit(X_train, y_train)

    y_pred = ridge.predict(X_test)
    return ridge.score(X_test, y_test)

[get_ridge_scores(alpha, X_train, X_test, y_train, y_test) for alpha in alphas]

# %%

from sklearn.linear_model import Lasso

alphas = [0.1, 1, 10, 20, 50]

def get_lasso_scores(alpha, X_train, X_test, y_train, y_test):
    lasso = Lasso(alpha = alpha).fit(X_train, y_train)

    y_pred = lasso.predict(X_test)
    return lasso.score(X_test, y_test)

[get_lasso_scores(alpha, X_train, X_test, y_train, y_test) for alpha in alphas]
# %%
# Lasso --> for feature selection
x = diabetes.drop('glucose', axis = 1)
X = x.values
names = x.columns
y = diabetes['glucose'].values

alphas = 10 ** np.arange(-3.0, 4.0)

res = {a:Lasso(alpha = a).fit(X, y).coef_ for a in alphas}

coef_df = pd.DataFrame().from_dict(
    res, 
    orient = 'index', 
    columns = names
).reset_index(
    drop = False, 
    names = 'alpha'
).melt(
    id_vars = 'alpha',
    var_name = 'IVs'
)
# Lasso(alpha = 0.1).fit(X, y).coef_

coef_df['alpha'] = coef_df['alpha'].astype('str')

px.bar(
    data_frame = coef_df,
    x = 'IVs',
    y = 'value',
    color = 'alpha'
).update_layout(
    barmode = 'group'
)

# dont stack values --> hide them behind 1 another
# set descrete color palette for alpha


# %%
