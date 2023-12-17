# project.py

from ui import landing_page
from calculators import drip_flow, steroid_conv, crcl_cg, egfr_ckd_2021, egfr_mdrd, qt_bazett, qt_friderica
from calculators import qt_framingham, qt_hodges, acsvd_risk, r_ipss, wpss, half_life, corr_calcium, anion_gap, weight_bmi, weight_ibw # Split import into two lines due to length

def main():
    # Display landing page, obtain user selection, and return user selection
    calculator_name = landing_page.main()

    # Dependency to call respective function to handle user selection
    calculator_dict = {
        "Drip and Flow rate" : drip_flow.main,
        "Steroid Conversion" : steroid_conv.main,
        "CrCl - Cockcroft-Gault" : crcl_cg.main,
        "eGFR - CKD-EPI" : egfr_ckd_2021.main,
        "eGFR - MDRD" : egfr_mdrd.main,
        "QTc - Bazett":  qt_bazett.main,
        "QTc - Friderica":  qt_friderica.main,
        "QTc - Framingham":  qt_framingham.main,
        "QTc - Hodges":  qt_hodges.main,
        "ACSVD Risk Score" : acsvd_risk.main,
        "R-IPSS" : r_ipss.main,
        "WPSS" : wpss.main,
        "Half-Life" : half_life.main,
        "Corrected Calcium" : corr_calcium.main,
        "Anion Gap" : anion_gap.main,
        "Body Mass Index" : weight_bmi.main,
        "Ideal Body Weight" : weight_ibw.main
     }

    if calculator_name in calculator_dict:
        calculator_dict[calculator_name]()

if __name__ == "__main__":
    main()
