from pathlib import Path
import numpy as np
import pandas as pd

def checkFx():
    print('hello there')

# filename_string = 'google.csv'
# filename_string = 'ozone'
def getFilePaths(filename_string, course_folder = 'Time_Series'):
    repo_home = Path().resolve().cwd()
    python_path = repo_home.joinpath('DataCamp/Python')

    return list(python_path.joinpath(course_folder).rglob(f'*/{filename_string}*'))

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

def getGoogleStockData():
    goog = getData('google.csv')
    goog['Date'] = pd.to_datetime(goog['Date'])

    newnames = {
        "Date": "date",
        "Close": "price"
    }

    goog.rename(columns = newnames, inplace = True)
    goog.set_index('date', inplace = True)

    goog = goog.asfreq('B')

    goog['price_l1'] = goog['price'].shift(periods = 1)

    goog.loc[goog['price'].isna(), 'price'] = goog.loc[goog['price'].isna(), 'price_l1']
    goog['price_l1'] = goog['price'].shift(periods = 1)

    goog['change'] = goog['price'].div(goog['price_l1'])

    goog['return'] = (goog['change'] - 1) * 100

    return goog[['price', 'return']]
