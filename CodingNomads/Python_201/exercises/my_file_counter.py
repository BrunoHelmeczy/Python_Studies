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

def writeFileCount2File(filename = 'check.csv', pretty = False):
    home = pathlib.Path.home()
    DataFolder = home / 'Desktop' / 'My_Professional_Development' / 'Python_Studies' / 'CodingNomads' / 'Python_201' / 'data'
    DataFolder.mkdir(exist_ok = True)
    cwd = os.getcwd()
    os.chdir(DataFolder)

    isNewFile = open(filename, 'r').read() == ''
    # myfile = open(filename, 'r')
    # myfile = open(filename, 'a')
    with open(filename, 'a') as myfile:
        filecount = countFilesUnderDesktop()
        TimeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if pretty == True:
            if isNewFile:
                headers = str([x for x in filecount.keys()]).replace("'", '').replace('[', '').replace(']', '') + '\n'
                myfile.write(headers)

            data = str([x for x in filecount.values()]).replace("'", '').replace('[', '').replace(']', '') + '\n'
            myfile.write(data)

        else:
            myfile.write(f"\n{TimeNow}: {str(filecount)}")
        # myfile.close()

    os.chdir(cwd)

def readFileCountFile(filename = 'check.txt'):
    home = pathlib.Path.home()
    DataFolder = home / 'Desktop' / 'My_Professional_Development' / 'Python_Studies' / 'CodingNomads' / 'Python_201' / 'data'
    DataFolder.mkdir(exist_ok = True)
    cwd = os.getcwd()
    os.chdir(DataFolder)

    with open(filename, 'r') as myfile:
        content = myfile.read()
        contlist = content.split('\n')

    splits = [s.strip() for s in re.sub('^.+ {(.+)}$', '\\1', contlist[-1]).split(',')]
    origdict = {x.split(':')[0].replace("'",''): int(x.split(':')[1]) for x in splits}

    os.chdir(cwd)

    return sum(origdict.values())

writeFileCount2File(pretty = True)
readFileCountFile()

# pathlib.Path().parent.resolve()
# datafolder = pathlib.Path().resolve()

# chk2 = datafolder.joinpath('input.txt').open()
# chk2.write('random 3rd line')
# chk2.close()
# print(chk2.readlines())

# chk = open(datafolder.joinpath('input.txt'), 'r')
# print(chk.readlines())
# print(chk.readline())
# chk.close()
