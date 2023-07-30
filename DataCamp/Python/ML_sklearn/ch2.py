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
