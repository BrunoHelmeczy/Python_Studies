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
    test_size = 0.1,
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

