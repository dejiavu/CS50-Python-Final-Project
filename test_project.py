# test_project.py

import sys
sys.path.append('/workspaces/58268113/project')

from tests.test_acsvd_risk import test_acsvd_risk
from tests.test_anion_gap import test_anion_gap
from tests.test_corr_calcium import test_corr_calcium
from tests.test_crcl_cg import test_crcl_cg
from tests.test_drip_flow import test_drip_flow
from tests.test_egfr_ckd_2021 import test_egfr_ckd_2021
from tests.test_egfr_mdrd import test_egfr_mdrd
from tests.test_half_life import test_half_life
from tests.test_qt_bazett import test_qt_bazett
from tests.test_qt_framingham import test_qt_framingham
from tests.test_qt_friderica import test_qt_friderica
from tests.test_qt_hodges import test_qt_hodges
from tests.test_r_ipss import test_r_ipss
from tests.test_steroid_conv import test_steroid_conv
from tests.test_weight_bmi import test_weight_bmi
from tests.test_weight_ibw import test_weight_ibw
from tests.test_wpss import test_wpss

test_acsvd_risk()
test_anion_gap()
test_corr_calcium()
test_crcl_cg()
test_drip_flow()
test_egfr_ckd_2021()
test_egfr_mdrd()
test_half_life()
test_qt_bazett()
test_qt_framingham()
test_qt_friderica()
test_qt_hodges()
test_r_ipss()
test_steroid_conv()
test_weight_bmi()
test_weight_ibw()
test_wpss()
