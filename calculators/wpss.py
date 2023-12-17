# calculators.wpss.py
import textwrap

"""
Equation to obtain WPSS (WHO prognostic scoring system) risk score

:param who_cat: WHO category
:param karyo: Karyotype
:param transf: Tranfusion status (Y/N)
"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, *result)

def get_user_input():
    while True:
        try:
            who_input = textwrap.dedent("""\
            WHO CATEGORY
            [1] Refractory anemia (RA), refractory anemia with ringed sideroblasts (RARS), or MDS with isolated del (5q)
            [2] Refractory cytopenia with multilineage dysplasia (RCMD), or refractory cytopenia with multilineage dysplasia and ringed sideroblasts (RCMD-RS)
            [3] Refractory anemia with excess of blasts, 2-4% blasts in peripheral blood (RAEB-1)
            [4] Refractory anemia with excess of blasts, 5-19% blasts in peripheral blood (RAEB-2)
            Enter corresponding 'number' from WHO category in list above = """)
            who_cat = int(input(who_input).strip())
            if who_cat not in range(1, 5):
                print("Invalid number entry. Please enter a valid input\n")
                continue
            break
        except ValueError:
            print("Invalid WHO category. Please enter a valid input\n")

    while True:
        try:
            karyo_input = textwrap.dedent("""\n
            KARYOTYPE
            [1] Good [normal, -Y, del(5q), del(20q)]
            [2] Poor [complex (≥3 abnormalities), chromosome 7 anomalies]
            [3] Intermediate [all other abnormalities]
            Enter corresponding 'number' from karyotype category in list above = """)
            karyo_cat = int(input(karyo_input).strip())
            if who_cat not in range(1, 4):
                print("Invalid number entry. Please enter a valid input\n")
                continue
            break
        except ValueError:
            print("Invalid karyotype. Please enter a valid input\n")

    while True:
        try:
            transf = input("If the patient had at least one RBC transfusion every 8 weeks over a period of 4 months, enter Y, otherwise, enter N = ")
            if transf not in ["Y", "N"]:
                print("Transfusion status is incorrectly inputed")
                continue
            break
        except ValueError:
            print("Invalid karyotype. Please enter a valid input\n")

    return who_cat, karyo_cat, transf

def calc_user_input(who_cat, karyo_cat, transf):
    who_value = who_cat - 1
    karyo_value = karyo_cat - 1
    transf_value = 1 if transf == "Y" else 0
    risk_score = who_value + karyo_value + transf_value

    # Derive WPSS "risk category"
    if risk_score == 0:
        risk_cat = "Very Low"
    elif risk_score ==1:
        risk_cat = "Low"
    elif risk_score == 2:
        risk_cat = "Intermediate"
    elif 3 <= risk_score < 5:
        risk_cat = "High"
    else:
        risk_cat = "Very High"

    return risk_score, risk_cat

def print_result(who_cat, karyo_cat, transf, risk_score, risk_cat):
    # Convert numeric WHO category selection value to text (for print out)
    if who_cat == 1:
        who_cat = "Refractory anemia (RA), refractory anemia with ringed sideroblasts (RARS), or myelodysplastic syndrome with isolated del (5q)"
    elif who_cat == 2:
        who_cat = "Refractory cytopenia with multilineage dysplasia (RCMD), or refractory cytopenia with multilineage dysplasia and ringed sideroblasts (RCMD-RS)"
    elif who_cat == 3:
        who_cat = "Refractory anemia with excess of blasts, 2-4% blasts in peripheral blood (RAEB-1)"
    else:
        who_cat = "Refractory anemia with excess of blasts, 5-19% blasts in peripheral blood (RAEB-2)"

    # Convert numeric karyotype selection value to text (for print out)
    if karyo_cat == 1:
        karyo_cat = "Good"
    elif karyo_cat == 2:
        karyo_cat = "Intermediate"
    else:
        karyo_cat = "Poor"

    # Convert transfusion selection value to text (for print out)
    if transf == 1:
        transf = "Regularly transfused"
    else:
        transf = "Non-regularly transfused"

    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

# who_cat, karyo_cat, transf, who_value, karyo_value, transf_value

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"WHO Category = {who_cat}", RED))
    print(color_text(f"Karyotype Category = {karyo_cat}", RED))
    print(color_text(f"Transfusion Category = {transf}", RED))
    print(color_text(f"*** WPSS risk score = {risk_score} ***", BLUE))
    print(color_text(f"*** WPSS risk category = {risk_cat} ***\n", BLUE))

if __name__ == "__main__":
    main()
