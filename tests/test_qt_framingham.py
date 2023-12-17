# test_qt_framingham.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import qt_framingham

def test_qt_framingham():
    test_data = [
        ((65, 400), (412)),
        ((75, 410), (441)),
        ((85, 375), (420)),
        ((110, 390), (460))
    ]
    for input_data, output_expected in test_data:
        assert qt_framingham.calc_user_input(*input_data) == output_expected
