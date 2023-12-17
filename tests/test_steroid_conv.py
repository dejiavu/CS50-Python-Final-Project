# test_steroid_conv.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import steroid_conv

def test_steroid_conv():
    test_data = [
        (("Betamethasone", 0.75, "Cortisone", 25, 25), (833.3)),
        (("Dexamethasone", 0.75, "Prednisolone", 5, 45), (300.0)),
        (("MethylPrednisolone", 4, "Prednisolone", 5, 75), (93.8)),
        (("Prednisone", 5, "Dexamethasone", 0.75, 100), (15.0))
    ]
    for input_data, output_expected in test_data:
        assert steroid_conv.calc_user_input(*input_data) == output_expected
