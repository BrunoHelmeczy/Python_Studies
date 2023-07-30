import numpy as np
import pandas as pd
from pathlib import Path
from os import listdir, getcwd

def getData(csv_name, folder):

    if getcwd().split('\\')[-1] == 'Python_Studies':
        data_folder = Path().resolve().joinpath(f'DataCamp/Python/{folder}/data')
    else: 
        data_folder = Path().resolve().joinpath('data')

    csvs = listdir(data_folder)

    if csv_name not in csvs:
        csv_text = f'Select from these available files: \n{csvs}'
        data_text = f'Alternatively, move your file in the data folder: \n{data_folder}'

        return print(f'Error: "{csv_name}" is not present in the data folder. \n\n{csv_text} \n\n{data_text}\n')
    
    return pd.read_csv(
        data_folder.joinpath(csv_name)
    )

def get_all_data_dfs(relpath):
    filepaths = list(Path().resolve().joinpath(relpath).rglob('data/*'))
    files = [f.as_uri().split('/')[-1] for f in filepaths]

    return {f.strip('.csv'):getData(f, 'ML_sklearn') for f in files}
