# test_egfr_ckd_2021.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import egfr_ckd_2021

def test_egfr_ckd_2021():
    test_data = [
        ((25, 1.2, "M"), (86)),
        ((40, 1.4, "F"), (49)),
        ((60, 0.85, "M"), (99)),
        ((85, 0.6, "F"), (88))
    ]
    for input_data, output_expected in test_data:
        assert egfr_ckd_2021.calc_user_input(*input_data) == output_expected
