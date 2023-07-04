from pathlib import Path
import pandas as pd

def checkFx():
    print('hello there')

def getData(filename_string, course_folder = 'Time_Series'):
    repo_home = Path().resolve().cwd()
    python_path = repo_home.joinpath('DataCamp/Python')

    my_files = list(python_path.joinpath(course_folder).rglob(f'*/{filename_string}'))[0]

    format = filename_string.split('.')[-1]

    if format == 'csv':
        my_fx = pd.read_csv
    else:
        my_fx = pd.read_excel

    return my_fx(
        my_files
    )
