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
