# %%
REL_PATH = 'DataCamp/Python/ML_sklearn'
import sys
sys.path.append(REL_PATH)
from my_utils import *

import os
os.getcwd()

# %%
dfs = getData(all = True)
# getData('diabetes_clean.csv')

dfs.keys()

# %%
# 1.2) Classification Challenge
churn_df = dfs['telecom_churn_clean'].set_index(
    'Unnamed: 0', 
    drop = True
)

churn_df.index.names = ['ID']

from sklearn.neighbors import KNeighborsClassifier

# churn_df.columns
X = churn_df[['total_day_charge', 'total_eve_charge']].values
y = churn_df['churn'].values # in scikit-learn 1.3.0: 1d array; 
# y2 = churn_df['churn'].values.reshape(-1, 1) if subset as pd.Series --> .reshape(-1, 1) --> 2d np array
# (y == y2).all() # they're the same in the end

knn = KNeighborsClassifier(n_neighbors = 15)

knn.fit(X, y)

X_new = np.array([
    [56.8, 17.5],
    [24.4, 24.1],
    [50.1, 10.9]
])

y_pred = knn.predict(X_new)

# 1.2) Exercises

# from sklearn.neighbors import KNeighborsClassifier
X = churn_df[['account_length', 'customer_service_calls']].values
y = churn_df['churn'].values

knn = KNeighborsClassifier(n_neighbors = 6)

knn.fit(X = X, y = y)

X_new = np.array([
    [30.0, 17.5],
    [107.0, 24.1],
    [213.0, 10.9]
])

y_pred = knn.predict(X_new)

# 1.3) Measure Model Performance
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size = 0.3, 
    random_state = 42, 
    stratify = y
)

knn = KNeighborsClassifier(n_neighbors = 6).fit(X_train, y_train)

y_pred = knn.predict(X_test)
knn.score(X_test, y_test)

# accuracies = pd.DataFrame(columns = ['n_neighbors', 'train', 'test'])

accuracies = {}

knn_ns = np.arange(1, 26)

ns = 1
for ns in knn_ns:
    knn = KNeighborsClassifier(n_neighbors = ns).fit(
        X_train, y_train
    )

    row = {
        'n_neighbors': ns,
        'train': knn.score(X_train, y_train).round(3),
        'test': knn.score(X_test, y_test).round(3)
    }

    accuracies[ns] = row

res = pd.DataFrame.from_dict(accuracies, orient = 'index' )
res.sort_values(by = 'test', ascending = False)  


# %%
import plotly.express as px


# res.columns[1:] = 'acc_' + res.columns[1:]

df_long = pd.melt(
    frame = res,
    id_vars = ['n_neighbors'],
    var_name = 'sample',
    value_name = 'accuracy'
)

px.line(
    data_frame = df_long,
    x = 'n_neighbors'
    , y = 'accuracy'
    , color = 'sample'
    , title = 'KNN In/Out Sample Accuracies'
).update_layout(
    hovermode = 'x',
    legend = {
        'orientation': 'h',
        'x': 0.5,
        'xanchor': 'center'

    }
)


# %%
churn_df = dfs['telecom_churn_clean']
X = churn_df.drop('churn', axis = 1).values
y = churn_df['churn'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size = 0.3, 
    random_state = 42, 
    stratify = y
)

knn = KNeighborsClassifier(n_neighbors = 5).fit(X_train, y_train)

knn.score(X_test, y_test)

