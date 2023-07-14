# 3) Test organization & execution
import numpy as np
import pytest
import sys
sys.path.append('DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *
from src.data.train import *

# 3.1) Org. growing set of tests
# all code: src folder
# all test: tests folder 
    # on same level as src
    # mirror folder structure in src
    # Test organization: Test Classes
        # class per function to test

# class TestRowToList(object): 
    # Use CamelCase; Always put the arg object
    # def test_for_clean_row(self): 
        # Alwyas put the single argument self  
# run: py -m pytest <path/to/your/test/file.py>

# 3.2) Master test execution
# run all tests in test folder: `py -m pytest <path/to/inside/your/tests/folder>`
    # for this project: `py -m pytest Datacamp/Python/unit_testing/tests/`

    # recursively find & run all tests in subtree
    # ID test modules:  filenames       starting w `test_`
    # ID test classes:  classnames      starting w `Test`
    # ID unit tests:    function names  starting w `test_` 

# run tests/data: `py -m pytest DataCamp/Python?unit_testing/tests/data/`
# run a test class/unit test: Node IDs
    # class:            `py -m pytest DataCamp/Python?unit_testing/tests/data/test_preprocessing_helpers.py::TestRowToList`
    # test in class:    `py -m pytest DataCamp/Python?unit_testing/tests/data/test_preprocessing_helpers.py::TestRowToList::test_for_missing_area`

# stop after 1st failed test:   `py -m pytest -x <path/to/your/tests/bla.py>`
# find tests via keyword:       `py -m pytest -k "row" <path/to/your/tests/bla.py>`

