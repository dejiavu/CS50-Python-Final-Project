# test_wpss.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import wpss

def test_wpss():
    test_data = [
        ((1, 1, "Y"), (1, "Low")),
        ((2, 2, "N"), (2, "Intermediate")),
        ((3, 3, "Y"), (5, "Very High"))
        ]
    for input_data, output_expected in test_data:
        assert wpss.calc_user_input(*input_data) == output_expected
