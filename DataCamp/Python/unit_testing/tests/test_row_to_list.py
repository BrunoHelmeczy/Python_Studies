import sys # use for importing my_utils (á la other python modules)
import pytest

sys.path.append('../Python_Studies/DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *

def test_for_clean_row():
    assert row_to_list("2,081\t314,942\n") == ['2,081', '314,942']

def test_for_missing_area():
    assert row_to_list("\t293,410\n") is None

def test_for_missing_tab():
    assert row_to_list("1,463258,765\n") is None
