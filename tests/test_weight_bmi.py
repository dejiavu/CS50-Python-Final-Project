# test_weight_bmi.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import weight_bmi

def test_weight_bmi():
    test_data = [
        ((120, 70), (17.2, "Underweight")),
        ((140, 60), (27.3, "Overweight")),
        ((160, 70), (23.0, "Normal weight")),
        ((250, 70), (35.9, "Obese (Class 2)"))
    ]
    for input_data, output_expected in test_data:
        assert weight_bmi.calc_user_input(*input_data) == output_expected
