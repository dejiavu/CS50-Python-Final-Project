# test_half_life.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import half_life

def test_half_life():
    test_data = [
        ((100, 0.5, 2.5), (87)),
        ((1000, 10, 5), (250)),
        ((10000, 90, 10), (20)),
        ((100000, 100, 25), (6250))
    ]
    for input_data, output_expected in test_data:
        assert half_life.calc_user_input(*input_data) == output_expected
