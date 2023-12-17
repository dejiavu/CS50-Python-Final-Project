# calculators.r_ipss.py
import textwrap

"""
Equation to obtain R-IPSS (revised IPSS) risk score

:param hgb: Hemoglobin (g/dL)
:param anc: Absolute neutrophil count (ANC) (x10^9/L)
:param plt: Platelet (x10^9/L)
:param bmb: Bone marrow blast (%)
:param cyto: Cytogenetics

"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, *result)

def get_user_input(): # Can optionally add exceptions to handle ranges
    while True:
        try:
            hgb = float(input("Enter hemoglobin (g/dL) = ").strip())
            break
        except ValueError:
            print("Invalid hemoglobin. Please enter a valid input")

    while True:
        try:
            anc = float(input("Enter absolute neutrophil count [ANC] (x10^9/L) = ").strip())
            break
        except ValueError:
            print("Invalid ANC. Please enter a valid input")

    while True:
        try:
            plt = int(input("Enter platelet value (x10^9/L)= ").strip())
            break
        except ValueError:
            print("Invalid platelet. Please enter a valid input\n")

    while True:
        try:
            bmb = int(input("Enter bone marrow biopsy (%) = ").strip())
            if bmb < 0 or bmb > 100:
                print("Bone marrow biopsy is incorrectly inputed. Ensure to enter Bone marrow biopsy in percentage (%)\n")
                continue
            break
        except ValueError:
            print("Invalid Bone marrow biopsy. Please enter a valid input\n")

    # Cytogentics list (inserted prior to try-except block to avoid re-printing for incorrect entries)
    cyto_input = textwrap.dedent("""\
    CYTOGENTIC RISK GROUP
    [1] Very Good [-Y, del(11q)]
    [2] Good [Normal, del(5q), del(12p), del(20q), double including del(5q)]
    [3] Intermediate [del(7q), +8, +19, i(17q), any other single or double independent clones]
    [4] Poor [-7, inv(3)/t(3q)/del(3q), double including -7/del(7q), Complex: 3 abnormalities]
    [5] Very Poor [Complex: >3 abnormalities]
    Enter corresponding "number" from cytogentic category in list above = """)

    while True:
        try:
            cyto = int(input(cyto_input).strip())
            if cyto not in range(1, 6):
                print("Invalid number entry. Please enter a valid input\n")
                continue
            break
        except ValueError:
            print("Invalid cytogenic. Please enter a valid input\n")

    return hgb, anc, plt, bmb, cyto

def calc_user_input(hgb, anc, plt, bmb, cyto):

    # Derive IPSS-R prognostic "score values"
    hgb_value = 1.5 if hgb < 8 else 1 if hgb < 10 else 0
    anc_value = 0.5 if anc < 0.8 else 0
    plt_value = 1 if plt < 50 else 0.5 if plt < 100 else 0
    bmb_value = 0 if bmb <= 2 else 1 if bmb < 5 else 2 if bmb <= 10 else 3
    cyto_value = cyto - 1

    risk_score = hgb_value + anc_value + plt_value + bmb_value + cyto_value

    # Derive IPSS-R prognostic "risk category"
    if risk_score <= 1.5:
        risk_cat = "Very Low"
    elif 1.5 < risk_score <= 3:
        risk_cat = "Low"
    elif 3 < risk_score <= 4.5:
        risk_cat = "Intermediate"
    elif 4.5 < risk_score <= 6:
        risk_cat = "High"
    else:
        risk_cat = "Very High"

    return risk_score, risk_cat

def print_result(hgb, anc, plt, bmb, cyto, risk_score, risk_cat):
    # Convert numeric cytogentic selection value to text (for print out)
    if cyto == 1:
        cyto = "Very Good"
    elif cyto == 2:
        cyto = "Good"
    elif cyto == 3:
        cyto = "Intermediate"
    elif cyto == 4:
        cyto = "Poor"
    else:
        cyto = "Very Poor"

    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Hemoglobin = {hgb} g/dL", RED))
    print(color_text(f"Absolute Neutrophil Count (ANC) = {anc} x 10^9/L", RED))
    print(color_text(f"Platelets = {plt} x 10^9/L", RED))
    print(color_text(f"Bone marrow biopsy = {bmb}%", RED))
    print(color_text(f"Cytogenetics = {cyto}", RED))
    print(color_text(f"*** R-IPSS risk score = {risk_score} ***", BLUE))
    print(color_text(f"*** R-IPSS risk category = {risk_cat} ***\n", BLUE))

if __name__ == "__main__":
    main()

