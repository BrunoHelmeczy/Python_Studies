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
pens = getData('penguins.csv')
pens.columns

pens['Species'] = pens['Species'].str.replace(r' .+', '', regex = True)

# print(pens['Species'].unique())

px.scatter(
    data_frame = pens,
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
apple = getData('AAPL.csv')

px.line(
    data_frame = apple,
    x = 'Date',
    y = 'Close',
    title = '<b>AAPL</b> price'
)
# %%

go.Figure(
    go.Scatter(
        x = pens['Body Mass (g)'],
        y = pens['Flipper Length (mm)'],
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

# pens.columns
pen_flips = pens.assign(
    spec = pens[['Species']].replace(' .+', '', regex = True)
).groupby('spec', as_index = False).agg(
    av_flip_length = ('Flipper Length (mm)', np.mean)
)

px.bar(
    data_frame = pen_flips,
    x = 'spec',
    y = 'av_flip_length'
).update_layout(
    xaxis = {'title': {'text': 'Species'}},
    yaxis = {
        'title': {'text': 'Average <b>Flipper</b> Length'},
        'range': [150, pen_flips['av_flip_length'].max() + 30]
    }
)

# %%
px.line(
    data_frame = apple,
    x = 'Date',
    y = 'Close'
    , log_y = True
).update_layout(
    hovermode = 'x'
)

# %%
