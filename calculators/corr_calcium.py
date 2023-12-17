# calculators.corr_calcium.py
"""
Equation to calculate corrected calcium

:param calcium: Calcium (mg/dL)
:param albumin_pt: Patient's albumin (g/dL)
:param albumin_norm: Normal albumun value (g/dL)

"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            calcium = float(input("Enter calcium value (mg/dL) = ").strip())
            break
        except ValueError:
            print("Invalid calcium. Please enter a valid input")

    while True:
        try:
            albumin_pt = float(input("Enter patient's albumin value (g/dL) = ").strip())
            break
        except ValueError:
            print("Invalid albumin. Please enter a valid input")

    albumin_norm = 4 # Normal albumin in g/dL

    return calcium, albumin_pt, albumin_norm

def calc_user_input(calcium, albumin_pt, albumin_norm):
    result = (0.8 * (albumin_norm - albumin_pt)) + calcium
    return round(result, 1)

def print_result(calcium, albumin_pt, albumin_norm, result):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Calcium = {calcium} mg/dL", RED))
    print(color_text(f"Patient's albumin = {albumin_pt} g/dL", RED))
    print(color_text(f"Normal albumin level = {albumin_norm} g/dL", RED))
    print(color_text(f"*** Corrected albumin = {result} mg/dL ***\n", BLUE))

if __name__ == "__main__":
    main()
