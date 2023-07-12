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

# 4) copy the above to seperate file: ./tests/test_row_to_list.py
# 5) in CLI run: py -m pytest <path/to/your/test/file/test_row_to_list.py>
    # in iPython: !pytest <path/to/your/test/file/test_row_to_list.py>

# 1.3) test result reports
    # Section 1: general info: OS; rootdir; inifile; plugins;
    # Section 2: test results: 
        # collected ### items';
        # <path/to/test/file/filename.py> .F.     [100%]
            # .F. = Pass; Fail; Pass
            # Fails: raises AssertionError; can be other, e.g. NameError when none (instead of None)
    # Section 3: Info on FAILED tests
        # line with error : starts with '>'
        # calculation with error: starts with 'E'
        # line with 'where' in it shows returned values
    # Section 4: test result summary
        # Nr failed, Nr passed
        # tests run time: 0.08s

# 1.4) other test types



 
