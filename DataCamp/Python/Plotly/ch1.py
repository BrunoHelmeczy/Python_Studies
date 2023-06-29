# %%
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from statsmodels.formula.api import logit 
# from itertools import product
from pathlib import Path
from os import listdir, getcwd

# %%


# %% 
def getData(csv_name):

    if getcwd().split('\\')[-1] == 'Python_Studies':
        data_folder = Path().resolve().joinpath('DataCamp/Python/Plotly/data')
    else: 
        data_folder = Path().resolve().joinpath('data')

    csvs = listdir(data_folder)

    if csv_name not in csvs:
        csv_text = f'Select from these available files: \n{csvs}'
        data_text = f'Alternatively, move your file in the data folder: \n{data_folder}'

        return print(f'Error: "{csv_name}" is not present in the data folder. \n\n{csv_text} \n\n{data_text}\n')
    
    return pd.read_csv(
        data_folder.joinpath(csv_name)
    )

# rain = getData('rain.csv')


# %%

# barebones example
import plotly.graph_objects as go

monthly_sales = {
    'data': [{
        'type': 'bar', 
        'x': ['Jan', 'Feb', 'March'], 
        'y': [450, 475, 400]
    }],
    'layout': {'title': {'text': ''}}
}

fig = go.Figure(monthly_sales)

# fig

# %%
# shortcut: plotly.express
    # quick, minimal customizations
    # low-level: graph_objects (go.Bar(); go.Scatter())
import plotly.express as px

# UniVar Plots: Bar; Histogram; Box; Density
temps = pd.DataFrame({
    'day': ['M', 'T', 'W', 'Th', 'F', 'S', 'Sn'],
    'temp': [28, 27, 25, 31, 32, 35, 36]
})

px.bar(
    data_frame = temps,
    x = 'day',
    y = 'temp'
)

# %%
df = getData('penguins.csv')
# df.columns

px.histogram(
    data_frame = df,
    x = 'Body Mass (g)',
    # y = 'Body Mass (g)',
    # orientation = 'h',
    nbins = 10
)

# %%
px.box(
    data_frame = df,
    y = 'Flipper Length (mm)'
    # x = 'Flipper Length (mm)',
    # orientation = 'h'
)
# %%
revenues = df = getData('revenue_data.csv')

px.box(
    data_frame = df,
    y = 'Revenue',
    hover_data = ['Company']
)

# %%
px.histogram(
    data_frame = df,
    x = 'Revenue',
    nbins = 5
)

# %%

# color arg --> grouping variable
# color_discrete_map arg --> dict: var Value: 'rgb(X, X, X)' / 'red'/'green'/'blue'
# color scales: color_continuous_scale arg --> 
    # builtin ('inferno', 'plasma')
    # DIY:
my_scale = [('rgb(242, 238, 10)'), ('rgb(242, 95, 10)'), ('rgb(255, 0, 0)')] 

# df = getData('sydney_temps.csv')

px.bar(
    data_frame = temps,
    x = 'day',
    y = 'temp',
    color_continuous_scale = my_scale,
    color = 'temp'
)

# %%
scores = pd.DataFrame({
    'name': ['John', 'Julia', 'Xuan', 'Harry'],
    'score': [80, 97, 90, 85]
})

my_scale = ['rgb(255, 0, 0)', 'rgb(3, 252, 40)']

px.bar(
    data_frame = scores,
    x = 'name', 
    y = 'score',
    title = 'Student <b>Scores</b> by <b>Student</b>',
    color = 'score',
    color_continuous_scale = my_scale
)

# %%

revenues = getData('revenue_data2.csv')

revenues.loc[revenues['Revenue'] == 'Unknown', 'Revenue'] = None
revenues.dropna(subset = 'Revenue', inplace = True)
revenues['Revenue'] = revenues['Revenue'].astype('int')


inds = revenues['Industry'].unique()

colors = [
	 'rgb(124, 250, 120)', 
	 'rgb(112, 128, 144)', 
	 'rgb(137, 109, 247)', 
	 'rgb(255, 0, 0)',
	 'rgb(4, 25, 120)', 
	 'rgb(1, 28, 14)', 
	 'rgb(37, 19, 47)'
]

ind_color_map = {inds[i]: colors[i] for i in range(len(inds))}


px.box(
    data_frame = revenues,
    y = 'Revenue',
    x = 'Industry',
    color = 'Industry',
    color_discrete_map = ind_color_map
)


# %%
px.histogram(
    data_frame = revenues,
    x = 'Revenue',
    nbins = 5,
    color_discrete_map = ind_color_map,
    color = 'Industry'
)
# %%
