# 2) going further
import numpy as np
import pytest
import sys
sys.path.append('DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *
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