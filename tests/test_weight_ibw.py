# test_weight_ibw.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import weight_ibw

def test_weight_ibw():
    test_data = [
        (("M", 60), (110)),
        (("M", 80), (212)),
        (("F", 65), (126)),
        (("F", 70), (151))
    ]
    for input_data, output_expected in test_data:
        assert weight_ibw.calc_user_input(*input_data) == output_expected
