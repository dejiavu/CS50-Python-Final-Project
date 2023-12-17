# test_acsvd_risk.py
import sys
sys.path.append('/workspaces/58268113/project')
from calculators import acsvd_risk

def test_acsvd_risk():
    file_path = acsvd_risk.get_file_path()
    coeff_dict = acsvd_risk.get_coefficients(file_path)

    # Input sequence - sex, age, total_chol, hdl_chol, sbp, sbp_treated, smoke_yes, diab_yes
    test_data = [
        (("F", 30, 180, 45, 125, "N", "N", "N"), (1.31)),
        (("F", 50, 125, 55, 150, "Y", "Y", "N"), (8.81)),
        (("M", 75, 185, 35, 125, "Y", "Y", "Y"), (81.47)),
        (("M", 25, 100, 60, 135, "N", "N", "N"), (0.44))
    ]
    for input_data, output_expected in test_data:
        assert acsvd_risk.calc_user_input(*coeff_dict, *input_data) == output_expected
