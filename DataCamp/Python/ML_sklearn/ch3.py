# %%
REL_PATH = 'DataCamp/Python/ML_sklearn'
import sys
sys.path.append(REL_PATH)
from my_utils import *

import os
print(os.getcwd())

dfs = getData(all = True)

# %%
# 3.1) Model Evaluation
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

churn_df = dfs['telecom_churn_clean'].set_index(
    'Unnamed: 0', 
    drop = True
)

churn_df.index.name = 'ID'

X = churn_df.drop('churn', axis = 1).values
y = churn_df['churn'].values

# knn = KNeighborsClassifier(n_neighbors = 7).fit(X, y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size = 0.3,
    random_state = 42, 
    stratify = y
)

knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train)
y_pred = knn.predict(X_test)

# %%
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
# %%
# 3.2) ROC curve
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression().fit(X_train, y_train)


# %%
y_pred = logreg.predict(X_test)
y_pred_probs = logreg.predict_proba(X_test)[:, 1]

# %%
# vis ROC curve
from sklearn.metrics import roc_curve, roc_auc_score
import plotly.express as px

fpr, tpr, thresholds = roc_curve(y_test, y_pred_probs)
auc = roc_auc_score(y_test, y_pred_probs)

df = pd.DataFrame({
    'fpr':fpr,
    'ref_line': tpr,
    "tpr":tpr
}).melt(
    id_vars = ['tpr'],
    var_name = 'metric'
)

px.line(
    data_frame = df,
    x = 'value',
    y = 'tpr',
    color = 'metric'
).update_layout(
    xaxis = {'title': 'False Positive Rate', 'range': [0, 1]},
    yaxis = {'title': 'True Positive Rate', 'range': [0, 1]}, 
    hovermode = 'x'
    , annotations = [{
        'xref': 'paper',
        'yref' : 'paper',
        'x': 0.5,
        'y': 0.5,
        'xanchor': 'right',
        'yanchor': 'bottom',
        'text': f'AUC: <b>{auc.round(2)}</b>',
        'showarrow': False,
        'font': {
            'size': 16
        }
    }]
)

# %%
# Hyper param tuning:
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, KFold
from sklearn.linear_model import Ridge
kf = KFold(n_splits = 5, shuffle = True, random_state = 42)

param_grid = {
    'alpha': np.arange(0.0001, 1, 0.1),
    'solver': ['sag', 'lsqr']
}

np.arange(0.0001, 1, 0.1)

ridge = Ridge()

ridge_cv = GridSearchCV(ridge, param_grid, cv = kf)

ridge_cv.fit(X_train, y_train)

ridge_cv.best_params_
ridge_cv.best_score_

ridge2 = Ridge()

ridge_cv2 = RandomizedSearchCV(
    ridge2, param_grid, cv = kf, n_iter = 2
)

ridge_cv2.fit(X_train, y_train)

ridge_cv2.best_params_
ridge_cv2.best_score_

ridge_cv2.score(X_test, y_test)


# %%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso

diabetes = dfs['diabetes_clean']
X = diabetes.drop('diabetes', axis = 1).values
y = diabetes['diabetes'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size = 0.3, 
    random_state = 42, 
    stratify = y
)

param_grid = {
    'alpha': np.linspace(0.00001, 1, 20)
}

lasso = Lasso()

lasso_cv = GridSearchCV(
    lasso,
    param_grid,
    cv = kf
)

lasso_cv.fit(X_train, y_train)

lasso_cv.best_params_
lasso_cv.best_score_

# %%
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

params = {"penalty": ["l1", "l2"],
         "tol": np.linspace(0.0001, 1.0, 50),
         "C": np.linspace(0.1, 1, 50),
         "class_weight": ["balanced", {0:0.8, 1:0.2}]}

logreg_cv = RandomizedSearchCV(
    logreg,
    params,
    cv = kf
)

logreg_cv.fit(X_train, y_train)

logreg_cv.best_params_
logreg_cv.best_score_

