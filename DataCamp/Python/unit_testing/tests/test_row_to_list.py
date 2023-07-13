import sys # use for importing my_utils (á la other python modules)
import pytest

sys.path.append('../Python_Studies/DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *

# !!! not ideal to write expression 2x
# consider: expr = f''; actual = exec(expr) 
    # will not work with new line characters; probably most strings

def test_for_clean_row():
    expr = f'row_to_list("2,081\t314,942\n")'
    actual = row_to_list("2,081\t314,942\n")

    expected = ['2,081', '314,942']
    msg = f'{expr} is valid but did not return a list of length 2'
    assert actual == expected, msg

def test_for_missing_area():
    expr = f'row_to_list("\t293,410\n")'
    actual = row_to_list("\t293,410\n")

    expected = None
    msg = f"{expr} did not return None"
    assert actual is expected, msg

def test_for_missing_tab():
    expr = f'row_to_list("1,463258,765\n")'
    actual = row_to_list("1,463258,765\n")

    expected = None
    msg = f"{expr} did not return None"
    assert actual is expected, msg
