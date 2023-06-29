# %%
import os

if os.getcwd().split('\\')[-1] == 'Python_Studies':
    from DataCamp.Python.Plotly.my_utils import *
else:
    from my_utils import *

import plotly.express as px
import plotly.graph_objects as go

print(getData)

# %%
pens = df = getData('penguins.csv')
df.columns

df['Species'] = df['Species'].str.replace(r' .+', '', regex = True)

px.scatter(
    data_frame = df,
    x = 'Body Mass (g)',
    y = 'Flipper Length (mm)',
    color = 'Species',
    hover_data = ['Sample Number']
    # , hoverlabel = ''
    # , hovertemplate = '...'
).update_layout(
    hovermode = 'x',
    legend = {
        'orientation': 'h',
        'xanchor': 'center',
        'x': 0.5
    }
)

# %%
apple = df = getData('AAPL.csv')

px.line(
    data_frame = df,
    x = 'Date',
    y = 'Close',
    title = '<b>AAPL</b> price'
)
# %%

go.Figure(
    go.Scatter(
        x = df['Body Mass (g)'],
        y = df['Flipper Length (mm)'],
        mode = 'markers'
    )
)
# %%
go.Figure(
    go.Scatter(
        x = apple['Date'],
        y = apple['Close'],
        mode = 'lines'
    )
)

# %%
# correlation plot
cols = ['Flipper Length (mm)', 'Culmen Depth (mm)', 'Body Mass (g)', 'Delta 15 N (o/oo)']

cor_df = pens.loc[:, cols].dropna()

cors = cor_df.corr(method = 'pearson')

go.Figure(
    go.Heatmap(
        x = cors.columns,
        y = cors.columns,
        z = cors.values,
        colorscale = 'rdylgn',
        zmin = -1, 
        zmax = 1
    )
)

# %%
df = getData('world_bank_population.csv').dropna()

df.columns

cols = ['Country Name', 'Country Code', '']

# %%
