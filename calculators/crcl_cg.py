# calculators.crcl_cg.py
"""
Equation to calculate Creatinine Clearance based on Cockcroft-Gault Equation

:param age: Age (yrs)
:param weight: Weight (kg)
:param creatinine: Serum creatinine concetration (mg/dL)
:param Sex: Sex (M/F)

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
            weight = float(input("Enter weight (lbs) = ").strip())
            break
        except ValueError:
            print("Invalid weight. Please enter a valid input")

    while True:
        try:
            creatinine = float(input("Enter serum creatinine (mg/dL) = ").strip())
            break
        except ValueError:
            print("Invalid serum creatinine. Please enter a valid input")

    while True:
        try:
            sex = (input("Enter sex ('M' for male and 'F' for female) = ").strip().upper())
            if sex not in ["M", "F"]:
                print("Sex is incorrectly inputed, enter 'M' for male and 'F' for female")
                continue
            break
        except ValueError:
            print("Invalid sex. Please enter a valid input")

    return age, weight, creatinine, sex

def calc_user_input(age, weight, creatinine, sex):
    sex = 0.85 if sex == "F" else 1
    weight = weight / 2.20462 # Convert lbs to kg for equation
    result = ((140 - age) * (weight)* (sex) / (72 * creatinine))
    return round(result)

def print_result(age, weight, creatinine, sex, result):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Age = {age} years", RED))
    print(color_text(f"Weight = {weight} lbs", RED))
    print(color_text(f"Serum Creatinine = {creatinine} mg/dL", RED))
    print(color_text(f"Sex = {sex}", RED))
    print(color_text(f"*** Creatinine clearance (Cockcroft-Gault) = {result} mL/min ***\n", BLUE))

if __name__ == "__main__":
    main()
