import sys # use for importing my_utils (á la other python modules)
sys.path.append('../Python_Studies/DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *

# running a test: rows_to_list()
# 1) test_row_to_list.py
    # 'test_' indicates unit tests inside (naming convention)

# 2) import pytest module
import pytest

# 3) define tests
def test_for_clean_row():
    assert row_to_list("2,081\t314,942\n") == ['2,081', '314,942']

def test_for_missing_area():
    assert row_to_list("\t293,410\n") is None

def test_for_missing_tab():
    assert row_to_list("1,463258,765\n") is None

