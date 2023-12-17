# calculators.weight_bmi.py
"""
Equation to calculate Body Mass Index (BMI)

:param weight: Weight (lbs)
:param height: Height (inches)

"""
def main():
    user_input = get_user_input()
    result = calc_user_input(*user_input)
    print_result(*user_input, *result)

def get_user_input(): # Can optionally add exceptions to handle ranges below
    while True:
        try:
            weight = float(input("Enter weight(lbs) = ").strip())
            break
        except ValueError:
            print("Invalid weight. Please enter a valid input")

    while True:
        try:
            height = float(input("Enter height (inches) = ").strip())
            break
        except ValueError:
            print("Invalid weight. Please enter a valid input")

    return weight, height

def calc_user_input(weight, height):
    bsa = (weight / height ** 2) * 703
    print(bsa)

    # Derive delta ratio category
    if bsa < 18.5:
        bsa_cat = "Underweight"
    elif 18.5 <= bsa < 25.0:
        bsa_cat = "Normal weight"
    elif 25.0 <= bsa < 30.0:
        bsa_cat = "Overweight"
    elif 30.0 <= bsa < 35.0:
        bsa_cat = "Obese (Class 1)"
    elif 35.0 <= bsa < 40.0:
        bsa_cat = "Obese (Class 2)"
    else:
        bsa_cat = "Obese (Class 3)"

    return round(bsa, 1), bsa_cat

def print_result(weight, height, bsa, bsa_cat):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def color_text(text, color):
        return f"{color}{text}{RESET}"

    print(color_text("\nSummary of calculation", BOLD))
    print(color_text(f"Weight = {weight} lbs", RED))
    print(color_text(f"Height = {height} inches", RED))
    print(color_text(f"*** Body Mass Index = {bsa} kg/m^2 ({bsa_cat}) ***\n", BLUE))

if __name__ == "__main__":
    main()
