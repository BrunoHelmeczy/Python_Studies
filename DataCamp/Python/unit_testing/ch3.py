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

# 3.3) Expected failures & Conditional Skipping
# Expected failure:     @pytest.mark.xfail
    # show reason in CLI summary: `py -m pytest -rs <path/to/your/tests/...>` 
# Skip conditionally:   @pytest.mark.skipif(boolean_expr, reason = "write your reason here")
    # show reason in CLI summary: `py -m pytest -rs <path/to/your/tests/...>` 

# show both: `py -m pytest -rsx <path/to/your/tests/...>` 
class TestTrainModel(object):
    @pytest.mark.xfail(reason = "Using TDD, train_model() not implemented yet") # use if f(x) tested is not yet implemented
    def test_on_linear_data(self):
        test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected_slope = 2.0
        expected_intercept = 1.0
        actual_slope, actual_intercept = train_model(test_argument)
        slope_message = ("train_model({0}) should return slope {1}, "
                         "but it actually returned slope {2}".format(test_argument, expected_slope, actual_slope)
                         )
        intercept_message = ("train_model({0}) should return intercept {1}, "
                             "but it actually returned intercept {2}".format(test_argument,
                                                                             expected_intercept,
                                                                             actual_intercept
                                                                             )
                             )
        assert actual_slope == pytest.approx(expected_slope), slope_message
        assert actual_intercept == pytest.approx(expected_intercept), intercept_message

    @pytest.mark.skipif(sys.version_info > (2, 7), reason = 'runs in <= Python 2.7')
    def test_on_linear_data2(self):
        test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected_slope = 2.0
        expected_intercept = 1.0
        actual_slope, actual_intercept = train_model(test_argument)
        slope_message = ("train_model({0}) should return slope {1}, "
                         "but it actually returned slope {2}".format(test_argument, expected_slope, actual_slope)
                         )
        intercept_message = ("train_model({0}) should return intercept {1}, "
                             "but it actually returned intercept {2}".format(test_argument,
                                                                             expected_intercept,
                                                                             actual_intercept
                                                                             )
                             )
        assert actual_slope == pytest.approx(expected_slope), slope_message
        assert actual_intercept == pytest.approx(expected_intercept), intercept_message

# 3.4) CI & Code Coverage
