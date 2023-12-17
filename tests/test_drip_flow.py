# test_drip_flow.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import drip_flow

def test_drip_flow():
    test_data = [
        ((250, 10, 30), (83)),
        ((250, 15, 40), (94)),
        ((500, 20, 90), (111)),
        ((500, 20, 120), (83))
    ]
    for input_data, output_expected in test_data:
        assert drip_flow.calc_user_input(*input_data) == output_expected
