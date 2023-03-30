import pathlib
# find path to desktop
# list files in desktop
# filter for screenshots
# create new folder
# move screenshots to new folder

path = pathlib.Path.cwd()
str(path)

home = pathlib.Path.home()

home / 'Desktop' / 'My_Professional_Development'

desktop = home / 'Desktop'

[file for file in path.iterdir()]
[file.name for file in path.iterdir()]

[item for item in path.rglob('*')]
[item for item in path.rglob('DataCamp/**')]

[item if item.suffix == '.png' else None for item in path.rglob('*')]

from itertools import compress
list(compress(desktop.rglob('*'), [item if item.suffix == '.png' else None for item in desktop.rglob('*')]))

[item if item.suffix == '.png' else None for item in desktop.rglob('*')]
[item if item.suffix == '.png' else None for item in desktop.iterdir()]

screenshots = desktop / 'screenshots'
screenshots.mkdir(exist_ok = True)

