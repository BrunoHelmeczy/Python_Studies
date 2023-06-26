import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from pathlib import Path

data_folder = Path().resolve().joinpath('DataCamp/Python/Intro_Regressions/data')

fish = pd.read_csv(
    data_folder.joinpath('fish.csv')
)

# 1) simple lin regs

## Y ~ X (numeric)
lm_fish = ols(
    formula = "mass_g ~ length_cm",
    data = fish
).fit()

lm_fish.params

## Y ~ X (categorical)
lm_fish1 = ols(
    formula = 'mass_g ~ species',
    data = fish
).fit()

lm_fish1.params

## Y ~ X (categorical - without intercept)
lm_fish_1a = ols(
    formula = 'mass_g ~ species + 0',
    data = fish
).fit()

lm_fish_1a.params

# 2) extend 2 MLR
lm_fish_mlr = ols(
    formula = 'mass_g ~ length_cm + species + 0',
    data = fish
).fit()

lm_fish_mlr.params

lm_fish_mlr.summary()