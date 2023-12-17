# test_r_ipss.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import r_ipss

def test_r_ipss():
    test_data = [
        ((7.5, 5, 75, 1, 3), (4, "Intermediate")),
        ((8.5, 4, 150, 10, 4), (6, "High")),
        ((9.5, 3, 80, 0, 1), (1.5, "Very Low")),
        ((10.5, 1.5, 50, 25, 2), (4.5, "Intermediate"))
    ]
    for input_data, output_expected in test_data:
        assert r_ipss.calc_user_input(*input_data) == output_expected
