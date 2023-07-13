import sys # use for importing my_utils (á la other python modules)
import pytest

sys.path.append('../Python_Studies/DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *

# !!! not ideal to write expression 2x
# consider: expr = f''; actual = exec(expr) 
    # will not work with new line characters; probably most strings
def test_with_no_comma():
    expr = "756"
    actual = convert_to_int(expr)
    expected = 756
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'

def test_with_one_comma():
    expr = "2,081"
    actual = convert_to_int(expr)
    expected = 2081
    assert isinstance(actual, int), f'ReturnValue is not integer'
    assert actual == expected, f'ReturnValue unequal to Expectation; Expected: {expected}, Actual: {actual}'

def test_with_two_commas():
    expr = "1,034,891"
    actual = convert_to_int(expr)
    expected = 1034891
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'

def test_on_string_with_incorrectly_placed_comma():
    expr = "12,72,891"
    actual = convert_to_int(expr)
    expected = None
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'

def test_on_string_with_missing_comma():
    expr = "178100,301"
    actual = convert_to_int(expr)
    expected = None
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'

def test_on_float_valued_string():
    expr = "6.9"
    actual = convert_to_int(expr)
    expected = None
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'
