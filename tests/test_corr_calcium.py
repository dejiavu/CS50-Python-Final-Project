# test_corr_calcium.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import corr_calcium

def test_corr_calcium():
    test_data = [
        ((9, 3.5, 4), (9.4)),
        ((9.5, 4, 4), (9.5)),
        ((10, 4.5, 4), (9.6)),
        ((10.5, 5, 4), (9.7))
    ]
    for input_data, output_expected in test_data:
        assert corr_calcium.calc_user_input(*input_data) == output_expected
