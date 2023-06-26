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

# 1a) standard vis - simple lin reg
sns.regplot(
    x = 'length_cm',
    y = 'mass_g',
    data = fish,
    ci = None
)
plt.show()

sns.boxplot(
    x = 'species',
    y = 'mass_g',
    data = fish,
    showmeans = True
)
plt.show()

# extend to MLR - parallel slopes
sns.lmplot(
    x = 'length_cm',
    y = 'mass_g',
    data = fish,
    hue = 'species',
    fit_reg = False
)

coeffs = lm_fish_mlr.params
bream, perch, pike, roach, sl = coeffs

ics = [bream, perch, pike, roach]
colors = ['blue', 'green', 'red', 'orange']

[plt.axline(xy1 = (0, ics[i]), slope = sl, color = colors[i]) for i in range(len(colors))]

plt.show()

# extend to MLR - non-parallel slopes
sns.lmplot(
    x = 'length_cm',
    y = 'mass_g',
    data = fish,
    hue = 'species'
)

plt.show()

# gen. preds
from itertools import product

lengths = np.arange(5, 61, 5)
fishes = fish['species'].unique()

exp_data = pd.DataFrame(
    product( lengths, fishes),
    columns = ['length_cm', 'species']
)

