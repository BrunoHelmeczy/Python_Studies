# count all file types under your desktop 

import pathlib
from collections import Counter

def countFilesUnderDesktop():
    home = pathlib.Path.home()
    desktop = home / 'Desktop'
    allpaths = [p for p in desktop.rglob('*')]
    filefreqs = Counter([p.suffix for p in allpaths])
    filesout = dict(sorted(filefreqs.items(), key = lambda item: item[1], reverse = True))

    [print(f"I found {v} files with extension {k} under your Desktop") for k, v in filesout.items()]
    return filesout