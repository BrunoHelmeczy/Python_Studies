# %%
import os
from my_utils import *
# if os.getcwd().split('\\')[-1] == 'Python_Studies':
#     # from DataCamp.Python.Dash.my_utils import *
#     from my_utils import *
# else:
#     from my_utils import *

import plotly.express as px
import plotly.graph_objects as go

print(getData)

sales = getData('ecom_sales.csv')

bar_df = sales.groupby('Country', as_index = False).agg(
    nr_items = ('Quantity', 'sum'),
    total_sales = ('OrderValue', 'sum')
)

# %%
bar_fig = px.bar(
    data_frame = bar_df,
    x = 'total_sales',
    y = 'Country'
)
# %%
import dash
from dash import dcc

app = dash.Dash()

app.layout = dcc.Graph(
    id = 'example-graph',
    figure = bar_fig
)

if __name__ == '__main__':
    # app.run_server(
    #     debug = True
    # )
    app.run(
        port = '8080'

    )


