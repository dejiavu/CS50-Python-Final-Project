# calculators.anion_gap.py
"""
Equation to calculate Anion gap

:param sodium: Sodium (mEq/L)
:param chloride: Chloride (mEq/L)
:param bicarbonate: Bicarbonate (mEq/L)

"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, *result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            sodium = float(input("Enter sodium value (mEq/L) = ").strip())
            break
        except ValueError:
            print("Invalid sodium. Please enter a valid input")

    while True:
        try:
            chloride = float(input("Enter chloride value (mEq/L) = ").strip())
            break
        except ValueError:
            print("Invalid chloride. Please enter a valid input")

    while True:
        try:
            bicarbonate = float(input("Enter bicarbonate value (mEq/L) = ").strip())
            break
        except ValueError:
            print("Invalid bicarbonate. Please enter a valid input")

    return sodium, chloride, bicarbonate

def calc_user_input(sodium, chloride, bicarbonate):
    anion_gap = sodium - (chloride + bicarbonate)
    delta_gap = (anion_gap - 12) # 12 is normal anion gap
    delta_ratio = delta_gap / (24 - bicarbonate)

    # Derive delta ratio category
    if delta_ratio < 0.4:
        delta_ratio_cat = "Hyperchloremic normal anion gap acidosis"
    elif 0.4 <= delta_ratio < 1:
        delta_ratio_cat = "High anion gap and normal anion gap acidosis"
    elif 1 <= delta_ratio <= 2:
        delta_ratio_cat = "Pure anion gap acidosis"
    else:
        delta_ratio_cat = "High anion gap acidosis and a concurrent metabolic alkalosis or a pre-existing compensated respiratory acidosis"

    return round(anion_gap, 1), round(delta_gap, 1), round(delta_ratio, 1), delta_ratio_cat

def print_result(sodium, chloride, bicarbonate, anion_gap, delta_gap, delta_ratio, delta_ratio_cat):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Sodium = {sodium} mEq/L", RED))
    print(color_text(f"Chloride = {chloride} mEq/L", RED))
    print(color_text(f"Bicarbonate = {bicarbonate} mEq/L", RED))
    print(color_text(f"*** Anion gap = {anion_gap} mEq/L *** ", BLUE))
    print(color_text(f"*** Delta gap = {delta_gap} mEq/L *** ", BLUE))
    print(color_text(f"*** Delta ratio = {delta_ratio} *** ", BLUE))
    print(color_text(f"*** Intrepretation = {delta_ratio_cat} ***\n", BLUE))

if __name__ == "__main__":
    main()
