import sys # use for importing my_utils (á la other python modules)
import pytest

sys.path.append('../Python_Studies/DataCamp/Python/unit_testing')
from src.data.preprocessing_helpers import *

def test_with_no_comma():
    inp = '756'
    act = my_convert_to_int(inp)
    exp = 756

    assert act == exp, f'Expected {exp}, Act: {act}'

def test_with_one_comma():
    inp = '2,081'
    act = my_convert_to_int(inp)
    exp = 2081

    assert act == exp, f'Expected {exp}, Act: {act}'

def test_with_two_commas():
    inp = '1,034,891'
    act = my_convert_to_int(inp)
    exp = 1034891

    assert act == exp, f'Expected {exp}, Act: {act}'

def test_on_string_with_missing_comma():
    inp = '1781öö,3ö1'
    act = my_convert_to_int(inp)
    exp = None

    assert act is exp, f'Expected {exp}, Act: {act}'

def test_on_string_with_incorrectly_placed_comma():
    inp = "12,72,891"
    act = my_convert_to_int(inp)
    exp = None

    assert act is exp, f'Expected {exp}, Act: {act}'

def test_on_float_string():
    inp = '23,816.92'
    act = my_convert_to_int(inp)
    exp = None

    assert act is exp, f'Expected {exp}, Act: {act}'
