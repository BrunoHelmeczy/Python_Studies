# You just want to print out the name of the soup, but there's also this
# other message printing out when you run this script!
# Make the necessary edits in `codingnomads/cook.py` to avoid that extra
# print statement. You can't remove any code in `cook.py`,
# but you can add code.

import os
import pathlib

origcwd = pathlib.Path().resolve()
os.chdir(list(origcwd.rglob('Python_201/*/*/cod*'))[0])

from codingnomads.cook import soup
os.chdir(origcwd)

print(f"I like {soup}.")
