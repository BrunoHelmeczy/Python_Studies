import pandas as pd
from pathlib import Path
from os import listdir, getcwd

def getData(csv_name):

    if getcwd().split('\\')[-1] == 'Python_Studies':
        data_folder = Path().resolve().joinpath('DataCamp/Python/Plotly/data')
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
