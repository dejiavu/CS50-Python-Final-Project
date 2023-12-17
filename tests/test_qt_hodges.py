# test_qt_hodges.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import qt_hodges

def test_qt_hodges():
    test_data = [
        ((65, 400), (409)),
        ((75, 410), (436)),
        ((85, 375), (419)),
        ((110, 390), (478))
    ]
    for input_data, output_expected in test_data:
        assert qt_hodges.calc_user_input(*input_data) == output_expected
