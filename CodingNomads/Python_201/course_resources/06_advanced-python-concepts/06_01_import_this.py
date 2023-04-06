# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.

import pathlib
import os

origcwd = pathlib.Path().resolve()
codingnomadspath = list(origcwd.rglob('*201/*/06_*/'))[0]

os.chdir(path = codingnomadspath)
from codingnomads.recipes.soup import make_soup
from codingnomads.ingredients import potato

os.chdir(origcwd)

soup = make_soup(potato)
print(soup)
