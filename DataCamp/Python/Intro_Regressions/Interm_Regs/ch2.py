import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from pathlib import Path
from itertools import product

data_folder = Path().resolve().joinpath('DataCamp/Python/Intro_Regressions/data')

fish = pd.read_csv(
    data_folder.joinpath('fish.csv')
)

# adding interactive terms
# implicit: x1 * x2
# explicit: x1 + x2 + x1:x2

fish.columns

lm_fish_mlr2 = ols(
    formula = 'mass_g ~ length_cm * species',
    data = fish
).fit()

coeffs = lm_fish_mlr2.params
# type(coeffs) # pd series
# a, b, c, d, e, f, g, h = coeffs

lm_fish_mlr2_ck = ols(
    formula = 'mass_g ~ length_cm + species + length_cm:species',
    data = fish
).fit()

(lm_fish_mlr2_ck.params == lm_fish_mlr2.params).all()


fish['species'].unique()
lengths = fish[['length_cm']].describe().loc[['min', 'max'], 'length_cm']
# type(lengths)

lng_min, lng_max = lengths

exp_data = pd.DataFrame(
    product(
        fish['species'].unique(), 
        np.arange(min([lng_min, 5]), lng_max + 5, 5)
    ),
    columns = ['species', 'length_cm']
)

pred_data = exp_data.assign(
    mass_g = lm_fish_mlr2.predict(exp_data)
)
