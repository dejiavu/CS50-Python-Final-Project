# test_crcl_cg.py
import sys
sys.path.append('/workspaces/58268113/project') # Ensure modules directory is in python file path
from calculators import crcl_cg

def test_crcl_cg():
    test_data = [
        ((35, 170, 0.8, "M"), (141)),
        ((45, 150, 1.2, "M"), (75)),
        ((55, 130, 1.5, "F",), (39)),
        ((75, 110, 0.8, "F",), (48))
    ]
    for input_data, output_expected in test_data:
        assert crcl_cg.calc_user_input(*input_data) == output_expected
