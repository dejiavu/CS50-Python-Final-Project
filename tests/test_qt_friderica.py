# test_qt_friderica.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import qt_friderica

def test_qt_friderica():
    test_data = [
        ((65, 400), (411)),
        ((75, 410), (442)),
        ((85, 375), (421)),
        ((110, 390), (477))
    ]
    for input_data, output_expected in test_data:
        assert qt_friderica.calc_user_input(*input_data) == output_expected
