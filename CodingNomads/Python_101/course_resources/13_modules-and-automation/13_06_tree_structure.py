# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib
from itertools import compress

home = pathlib.Path.home()
desktop = home / 'Desktop'

allPyFilesUnderDesktop = list(
    compress(
        desktop.rglob('*'),
        [f if f.suffix == '.py' else None for f in desktop.rglob('*')]
    )
)

