# %%
import os

if os.getcwd().split('\\')[-1] == 'Python_Studies':
    from DataCamp.Python.Plotly.my_utils import *
else:
    from my_utils import *

import plotly.express as px
import plotly.graph_objects as go

print(getData)

# %% [markdown]
'''
subplots: 
    plotly.express (px) --> add_trace()
        * complex code
        * not best practice (?)
    plotly.graph_objects (go)
'''


# %%
# create 1x2 subplot (hist + box)
rev = getData('revenue_data2.csv')

rev.loc[rev['Revenue'] == 'Unknown', 'Revenue'] = None
rev = rev.dropna(subset = 'Revenue')

rev['Revenue'] = rev['Revenue'].astype('int')
# rev.astype({'Revenue': 'int'})

from plotly.subplots import make_subplots
fig = make_subplots(
    rows = 2, cols = 1,
    subplot_titles = [
        'Histogram of company revenues',
        'Box plot of company revenues'
    ],
    shared_xaxes = True
)

fig.add_trace(
    go.Histogram(
        x = rev['Revenue'], 
        nbinsx = 5
    ),
    row = 1, col = 1
).add_trace(
    go.Box(
        x = rev['Revenue'],
        hovertext = rev['Company']
    ),
    row = 2, col = 1
).update_layout(
    showlegend = False,
    title = {
        'text': 'Plots of company revenues',
        'x': 0.5, 'y': 0.9
    }
)

# %%

pens = getData('penguins.csv')
pens['Species'] = pens['Species'].replace(' .+', '', regex = True)

fig = make_subplots(
    rows = 3, cols = 1,
    shared_xaxes = True
)
row_nr = 1

# pens.columns

for species in pens['Species'].unique():
    df = pens[pens['Species'] == species]

    fig.add_trace(
        go.Scatter(
            x = df['Culmen Length (mm)'],
            y = df['Culmen Depth (mm)'],
            name = species,
            mode = 'markers'
        ),
        row = row_nr, col = 1
    )
    row_nr += 1

fig.update_layout(
    hovermode = 'x',
    legend = {
        'orientation': 'h',
        'xref': 'paper', 'xanchor': 'center', 'x': 0.5
    }
)

# %%
# over-laying plots --> keep adding traces:
    # fig = go.Figure()
    # fig.add_trace(
    #   go.Scatter/Bar/Histogram: (
    #   x = df['col_name'],
    #   y = df['col_name'],
    #   name = 'trace_name' 
    #   )
    # )

# %%
# Time buttons (?) (+ rangeslider)
rain = getData('rain.csv')
rain['Date'] = pd.to_datetime(rain['Date'], format = "%d/%m/%y")

buttons = [
    {'count': 6,  'step': "month", "stepmode": "todate", "label": "6MTD"},
    {'count': 14, 'step': "day"  , "stepmode": "todate", "label": "2wks"}
]

# rain.columns
px.line(
    data_frame = rain,
    x = 'Date',
    y = 'Rainfall',
    title = 'Rainfall (mm) in Sydney'
).update_layout(
    xaxis = {
        'rangeselector': {'buttons': buttons},
        'rangeslider': {
            'visible': True,
            'thickness': 0.08
        },
        'type': 'date'
    },
    hovermode = 'x'
)

# %%
