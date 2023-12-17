# calculators.weight_ibw.py
"""
Equation to calculate Ideal Body Weight (IBW)

:param sex: Sex (M/F)
:param height: Height (inches)

"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            sex = (input("Enter sex ('M' for male and 'F' for female) = ").strip().upper())
            if sex not in ["M", "F"]:
                print("Sex is incorrectly inputed, enter 'M' for male and 'F' for female")
                continue
            break
        except ValueError:
            print("Invalid sex. Please enter a valid input")

    while True:
        try:
            height = float(input("Enter height (inches) = ").strip())
            break
        except ValueError:
            print("Invalid weight. Please enter a valid input")

    return sex, height

def calc_user_input(sex, height):
    if sex == "M":
        ibw = 50 + (2.3 * (height - 60))
    else:
        ibw = 45.5 + (2.3 * (height - 60))

    ibw = ibw * 2.20462 # Converts from kg to lbs

    return round(ibw)

def print_result(sex, height, ibw):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Sex = {sex}", RED))
    print(color_text(f"Height = {height} inches", RED))
    print(color_text(f"*** Ideal Body Weight (lbs) = {ibw} ***\n", BLUE))

if __name__ == "__main__":
    main()
