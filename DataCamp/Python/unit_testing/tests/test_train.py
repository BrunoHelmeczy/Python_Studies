import sys # use for importing my_utils (á la other python modules)
import pytest

sys.path.append('../Python_Studies/DataCamp/Python/unit_testing')
from src.data.train import *

def test_on_six_rows():
    test_argument = np.array([[2081.0, 314942.0],
                            [1059.0, 186606.0],
                            [1148.0, 206186.0],
                            [1506.0, 248419.0],
                            [1210.0, 214114.0],
                            [1697.0, 277794.0],
                            ]
                            )
    expected_length_training_set = 4
    expected_length_testing_set = 2
    actual = split_into_training_and_testing_sets(test_argument)
    assert actual[0].shape[0] == expected_length_training_set, \
            "The actual number of rows in the training array is not 4"
    assert actual[1].shape[0] == expected_length_testing_set, \
            "The actual number of rows in the testing array is not 2"

def test_valueerror_on_1_dim_arg():
    eg_arg = np.array([2081, 314942, 1059, 186606, 1148, 206186])

    with pytest.raises(ValueError) as exc_info:
        # Does nothing on entering context
        print("This is part of the context") # any code inside is the context

        split_into_training_and_testing_sets(eg_arg)

        # if context raised ValueError, silences it.
        # if context did not raise ValueError, raises exception
    exp_msg = "Argument data_array must be two dimensional. Got 1 dimensional array instead!"

    assert exc_info.match(exp_msg)
