REL_PATH = 'DataCamp/Python/ML_sklearn'

import sys
sys.path.append(REL_PATH)
from my_utils import *

dfs = get_all_data_dfs(REL_PATH)

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
