# test_qt_bazett.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import qt_bazett

def test_qt_bazett():
    test_data = [
        ((65, 400), (416)),
        ((75, 410), (458)),
        ((85, 375), (446)),
        ((110, 390), (528))
    ]
    for input_data, output_expected in test_data:
        assert qt_bazett.calc_user_input(*input_data) == output_expected
