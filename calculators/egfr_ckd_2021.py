# calculators.egfr_ckd_2021.py
"""
Equation to calculate estimated GFR based on CKD-EPI 2021

:param age: Age (yrs)
:param creatinine: Serum creatinine concetration (mg/dL)
:param gender: Sex (M/F)

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
            print("Invalid serum creatinine. Please enter a valid input")

    return age, creatinine, sex

def calc_user_input(age, creatinine, sex):
    sex = 1.012 if sex == "F" else 1

    #Derive addditional parameters
    if sex == 1.012:
        value_a = 0.7
        value_b = -0.241 if creatinine <= 0.7 else -1.2
    elif sex == 1:
        value_a = 0.9
        value_b = -0.302 if creatinine <= 0.9 else -1.2

    result = 142 * ((creatinine / value_a) ** value_b) * (0.9938 ** age) * sex
    
    return round(result)

def print_result(age, creatinine, sex, result):
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
    print(color_text(f"*** eGFR (CKD-2021) = {result} mL/min ***\n", BLUE))

if __name__ == "__main__":
    main()
