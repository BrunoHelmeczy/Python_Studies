import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols # , logit
from itertools import product
from pathlib import Path
from os import listdir

def getData(csv_name):
    data_folder = Path().resolve().joinpath('DataCamp/Python/Intro_Regressions/data')
    csvs = listdir(data_folder)

    if csv_name not in csvs:
        csv_text = f'Select from these available files: \n{csvs}'
        data_text = f'Alternatively, move your file in the data folder: \n{data_folder}'

        return print(f'Error: "{csv_name}" is not present in the data folder. \n\n{csv_text} \n\n{data_text}\n')
    
    return pd.read_csv(
        data_folder.joinpath(csv_name)
    )


# 2 numerice Xs: 2d scatterplot + Y as color
taiwan_real_estate = getData('taiwan_real_estate2.csv')

taiwan_real_estate['sqrt_dist_to_mrt_m'] = taiwan_real_estate['dist_to_mrt_m'] ** 0.5

sns.scatterplot(
    x = 'n_convenience',
    y = 'sqrt_dist_to_mrt_m',
    data = taiwan_real_estate,
    hue = 'price_twd_msq'
)

plt.show()

grid = sns.FacetGrid(
    data = taiwan_real_estate,
    col = 'house_age_years',
    hue = 'price_twd_msq',
    col_wrap = 3,
    palette = 'plasma'
)

grid.map(
    sns.scatterplot,
    'n_convenience',
    'sqrt_dist_to_mrt_m'
)

plt.show()

# interactions with 2+ Xs

df = taiwan_real_estate
cols = list(df.columns)
Y = cols.pop(cols.index('price_twd_msq'))

form_str = Y + ' ~ (' + ' + '.join(cols) + ') ** 2 + 0'

new_form_str = form_str.replace('sqrt_dist_to_mrt_m', 'np.sqrt(dist_to_mrt_m)')

mlr_ints = ols(
    # formula = form_str,
    formula = new_form_str,
    data = taiwan_real_estate
).fit()

mlr_ints.summary()

exp_data = pd.DataFrame(
    product(
        np.arange(0, 11, 1),
        np.arange(0, 81, 10) ** 2,
        # np.arange(0, 81, 10),
        taiwan_real_estate['house_age_years'].unique()
    ),
    columns = ['n_convenience', 'dist_to_mrt_m', 
            #    'sqrt_dist_to_mrt_m', 
               'house_age_years']
)

mlr_ints.predict(exp_data)



