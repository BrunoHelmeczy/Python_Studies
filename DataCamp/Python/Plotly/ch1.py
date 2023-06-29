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
    nbins = 10
)

# %%
