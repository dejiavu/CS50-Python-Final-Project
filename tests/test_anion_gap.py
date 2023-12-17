# test_anion_gap.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import anion_gap

def test_anion_gap():
    test_data = [
        ((136, 98, 23), (15.0, 3.0, 3.0, "High anion gap acidosis and a concurrent metabolic alkalosis or a pre-existing compensated respiratory acidosis")),
        ((130, 100, 21), (9.0, -3.0, -1.0, "Hyperchloremic normal anion gap acidosis")),
        ((140, 105, 21), (14.0, 2.0, 0.7, "High anion gap and normal anion gap acidosis")),
        ((140, 105, 27), (8.0, -4.0, 1.3, "Pure anion gap acidosis"))
    ]
    for input_data, output_expected in test_data:
        assert anion_gap.calc_user_input(*input_data) == output_expected
