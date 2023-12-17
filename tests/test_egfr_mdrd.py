# test_efgr_mdrd.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import egfr_mdrd

def test_egfr_mdrd():
    test_data = [
        ((25, 0.75, "M", "N"), (127)),
        ((50, 1.1, "F", "Y"), (64)),
        ((75, 1.3, "m", "n"), (54)),
        ((80, 0.65, "F", "Y"), (106))
    ]
    for input_data, output_expected in test_data:
        assert egfr_mdrd.calc_user_input(*input_data) == output_expected
