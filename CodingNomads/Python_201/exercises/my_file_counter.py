# count all file types under your desktop 
import pathlib
import os
import re
from datetime import datetime
from collections import Counter

def countFilesUnderDesktop():
    home = pathlib.Path.home()
    desktop = home / 'Desktop'
    allpaths = [p for p in desktop.rglob('*')]
    filefreqs = Counter([p.suffix for p in allpaths])
    filesout = dict(sorted(filefreqs.items(), key = lambda item: item[1], reverse = True))

    [print(f"I found {v} files with extension {k} under your Desktop") for k, v in filesout.items()]
    return filesout

def writeFileCount2File(filename = 'check.txt'):
    home = pathlib.Path.home()
    DataFolder = home / 'Desktop' / 'My_Professional_Development' / 'Python_Studies' / 'CodingNomads' / 'Python_201' / 'data'
    DataFolder.mkdir(exist_ok = True)
    cwd = os.getcwd()
    os.chdir(DataFolder)

    myfile = open(filename, 'a')

    filecount = countFilesUnderDesktop()

    TimeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    myfile.write(f"\n{TimeNow}: {str(filecount)}")
    myfile.close()

    os.chdir(cwd)

def readFileCountFile(filename = 'check.txt'):
    home = pathlib.Path.home()
    DataFolder = home / 'Desktop' / 'My_Professional_Development' / 'Python_Studies' / 'CodingNomads' / 'Python_201' / 'data'
    DataFolder.mkdir(exist_ok = True)
    cwd = os.getcwd()
    os.chdir(DataFolder)

    myfile = open(filename, 'r')
    content = myfile.read()
    contlist = content.split('\n')

    splits = [s.strip() for s in re.sub('^.+ {(.+)}$', '\\1', contlist[-1]).split(',')]
    origdict = {x.split(':')[0].replace("'",''): int(x.split(':')[1]) for x in splits}

    myfile.close()
    os.chdir(cwd)

    return sum(origdict.values())

writeFileCount2File()
readFileCountFile()
