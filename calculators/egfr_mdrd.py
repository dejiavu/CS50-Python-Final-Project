# calculators.egfr_mdrd.py
"""
Equation to calculate estimated GFR based on CKD-EPI 2021

:param age: Age (yrs)
:param creatinine: Serum creatinine concetration (mg/dL)
:param gender: Sex (M/F)
:param race: Black race (Y/N)

"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            age = int(input("Enter age (yrs) = ").strip())
            break
        except ValueError:
            print("Invalid age. Please enter a valid input")

    while True:
        try:
            creatinine = float(input("Enter serum creatinine (mg/dL) = ").strip())
            break
        except ValueError:
            print("Invalid serum creatinine. Please enter a valid input")

    while True:
        try:
            sex = (input("Enter gender ('M' for male and 'F' for female) = ").strip().upper())
            if sex not in ["M", "F"]:
                print("Sex is incorrectly inputed, enter 'M' for male and 'F' for female")
                continue
            break
        except ValueError:
            print("Invalid sex value. Please enter a valid input")

    while True:
        try:
            race = (input("If race is black, enter Y, otherwise, enter N = ").strip().upper())
            if race not in ["Y", "N"]:
                print("Race value is incorrectly inputed. If race is black, enter 'Y', otherwise, enter 'N'")
                continue
            break
        except ValueError:
            print("Invalid race. Please enter a valid input")

    return age, creatinine, sex, race

def calc_user_input(age, creatinine, sex, race):
    sex = 0.742 if sex == "F" else 1
    race = 1.212 if race == "Y" else 1
    result = 175 * (creatinine ** -1.154) * (age ** -0.203 ) * race * sex
    return round(result)

def print_result(age, creatinine, sex, race, result):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Age = {age} years", RED))
    print(color_text(f"Serum Creatinine = {creatinine} mg/dL", RED))
    print(color_text(f"Sex = {sex}", RED))
    print(color_text(f"Race = {race}", RED))
    print(color_text(f"*** eGFR (CKD-2021) = {result} mL/min ***\n", BLUE))

if __name__ == "__main__":
    main()
