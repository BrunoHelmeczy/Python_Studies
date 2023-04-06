# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.

import os
import pathlib

origcwd = pathlib.Path().resolve()

os.chdir(list(origcwd.rglob('Python_201/*/*/cod*'))[0])

import recipes.soup as s
import ingredients as i

os.chdir(origcwd)

digestible = i.prepare(i.potato)
mix = i.carrot + i.potato + i.salt
soup = s.make_soup(mix)
print(soup)
