# 2) going further
import numpy as np
import pytest
import sys
sys.path.append('DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *
from src.data.train import *
# row_to_list('bla\tbla\n')

# 2.1) Assert statements
# basic: assert boolean_expr
# +1: assert boolean_expr, message (when raising AssertionError)
    # expr returned {smth} vs 

code = 'print("hello world")'
exec(code)

# error message recos:
# print all relevant variables to be debugged

# float return values (?)
0.1 + 0.1 + 0.1 == 0.3
# solution: # pytest.approx()
0.1 + 0.1 + 0.1 == pytest.approx(0.3)
np.array([0.1 + 0.1, 0.1 + 0.1 + 0.1]) == pytest.approx(np.array([0.2, 0.3]))

# many assertions in 1 test
    # test fails if either assertion fails
    # prep seperate messages per assertion

# 2.2) Testing for Exceptions
def my_test():
    with pytest.raises(ValueError): # pytest.raises(ValueError) = context_manager
        raise ValueError # context exits with ValueError
        # pytest.raises(ValueError) silences it

def my_test2():
    with pytest.raises(ValueError): # pytest.raises(ValueError) = context_manager
        pass # context exits without raising ValueError
        # pytest.raises(ValueError) raises Failed

def my_test3():
    eg_arg = np.array([2081, 314942, 1059, 186606, 1148, 206186])

    with pytest.raises(ValueError) as exc_info: # exc_info stores silenced ValueError
        split_into_training_and_testing_sets(eg_arg)
        # pytest.raises(ValueError) raises Failed

    exp_msg = "Argument data_array must be two dimensional. Got 1 dimensional array instead!"

    assert exc_info.match(exp_msg)

# my_test3()

# 2.3) Well-tested f(x)
# Well-tested == tested for each argument type:
    # bad arggument; special argument; normal argument

# bad args:
    # def: function raises exception (ValueError)
    # e.g. split_into_training_and_testing_sets(eg_arg)
        # eg_arg = 1 dimensional
        # eg_arg = 1 row only

# special args:
    # boundary values: 2d array w 2 rows --> train-test = 1-1
    # arg values for which f(x) has special logic
        # f(x) logic: 4 rows --> train-test = 3-1
            # special: train-test = 2-2
            # if 4 is special value --> 3; 5 rows are boundary values

# normal args: test 2-3 of them
    # not directly next to bad/special args

# 2.4) Test-Driven Development
    # Priority: 1) Feature dev 2) testing
    # TDD: Tests written 1st
        # Unit test writing time (part of implementation time)
        # Feature dev includes thinkging of:
            # Norm/Spec/Bad args; Return Values; Exceptions --> Clearer reqs for implementation
            # Clearer implementation reqs --> easier/faster implementation

# 2.4) Exercise: implement convert_to_int() via TDD
# 1) write tests
# 2) implement f(x)
# 3) ensure passing all tests
